from dataclasses import dataclass


@dataclass
class Meeting:
    id: str
    title: str
    date: str
    owner: str
