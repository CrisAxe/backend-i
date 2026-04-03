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
def get_solution(problem: str):
    """Return troubleshooting steps based on a problem keyword."""

    solutions = {
        "network": [
            "Check if the router is powered on",
            "Restart the router",
            "Check ethernet/Wi-Fi connection",
            "Update network drivers"
        ],
        "freeze": [
            "Close heavy applications",
            "Check RAM usage in Task Manager",
            "Restart the computer"
        ],
        "heating": [
            "Clean the computer fans",
            "Ensure proper ventilation",
            "Check CPU usage"
        ],
        "bluescreen": [
            "Update system drivers",
            "Run Windows memory diagnostic",
            "Check for hardware issues"
        ],
        "osslow": [
            "Disable startup programs",
            "Delete temporary files",
            "Scan for malware"
        ]
    }

    return solutions.get(problem.lower(), ["Problem not recognized."])
