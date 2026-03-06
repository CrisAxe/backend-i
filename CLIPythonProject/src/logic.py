from data import Problem

def create_problem(network, freeze, heating, bluescreen, osslow):
    """Create a Problem object."""

    return Problem(
        network=network,
        freeze=freeze,
        heating=heating,
        bluescreen=bluescreen,
        osslow=osslow
    )
def get_solution(problem: str) -> str:
    """Return a solution based on a problem keyword."""

    solutions = {
        "network": "Check your router, restart it, and verify your network drivers.",
        "freeze": "Close heavy applications and check your RAM usage.",
        "heating": "Clean your computer fan and ensure proper ventilation.",
        "bluescreen": "Update drivers and run a system diagnostic.",
        "osslow": "Disable startup programs and clean temporary files."
    }

    return solutions.get(problem.lower(), "Problem not recognized. Try: network, freeze, heating, bluescreen, osslow.")