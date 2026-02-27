from data.models import Meeting
from uuid import uuid4

def create(meeting:Meeting):
    BASE_PATH = "saves"
    filename = f"{BASE_PATH}/{uuid4()}.md"
    with open(filename,"w") as file:
        file.writelines(str(meeting))