from dataclasses import asdict
import json
from pathlib import Path

from data.models import Meeting,MeetingMetadata
from uuid import uuid4


BASE_PATH = Path ("saves")
INDEX_PATH = Path("saves/index.json")

def create(meeting:Meeting):
    filename = f"{BASE_PATH}/{uuid4()}.md"
    with open(filename,"w") as file:
        file.writelines(str(meeting))

    
    if not INDEX_PATH.exists():
        INDEX_PATH.touch()
        INDEX_PATH.write_text("[]")

    index_content = None

    with open(INDEX_PATH.absolute(),"r") as file:
        index_content:list = json.loads(file.read())

    index_content.append(
        asdict(MeetingMetadata(
            meeting=meeting,
            path=filename
        ))
    )
    
    with open(INDEX_PATH,"w") as file:
        json.dump(index_content,file)
    # index = []
    # for meeting in index_content:
    #     new_mm = MeetingMetadata(
    #         meeting=Meeting(
    #             title=meeting["meeting"]["title"]
    #             owner=meeting["meeting"]["owner"]
    #             date=meeting["meeting"]["date"]
    #         ),
    #         path=meeting["path"]
    #     )
    #     index.append(new_mm)
        
