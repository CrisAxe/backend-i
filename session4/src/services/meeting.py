from services import database
from data.models import Meeting

def create(title: str, owner: str,date:str):
    new_meeting= Meeting(
        title=title,
        owner=owner,
        date=date
    )
    database.create(new_meeting)
