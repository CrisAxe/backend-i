import json
from pathlib import Path
from data.models import Meeting
from uuid import uuid4


BASE_PATH = Path ("saves")
INDEX_PATH = Path("saves/index.json")

def create(meeting:Meeting):
    BASE_PATH = "saves"
    filename = f"{BASE_PATH}/{uuid4()}.md"
    with open(filename,"w") as file:
        file.writelines(str(meeting))

    
    if not INDEX_PATH.exists():
        INDEX_PATH.touch([])

    index_content = None
    breakpoint()
    with open(INDEX_PATH.absolut(),"r") as file:
        
        index_content = json.loads(file.read())
        
