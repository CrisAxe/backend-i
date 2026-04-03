import time
import uuid
import logging
from fastapi import Request

logger = logging.getLogger("request")


async def request_tracing_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start = time.time()

    response = await call_next(request)

    duration = round((time.time() - start) * 1000, 2)

    logger.info(
        "request completed",
        extra={
            "request_id": request_id,
            "method": request.method,
            "path": request.url.path,
            "status": response.status_code,
            "duration_ms": duration,
        },
    )

    response.headers["X-Request-ID"] = request_id
    return response
