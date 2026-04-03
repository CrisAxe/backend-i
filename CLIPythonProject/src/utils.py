from datetime import datetime

def log_problem(problem_str: str):
    """Append a problem report to the history file."""
    with open("problem_history.txt", "a") as f:
        f.write(f"{datetime.now()} - {problem_str}\n")