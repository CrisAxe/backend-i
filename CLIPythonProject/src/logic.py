from data import Problem
from dataclasses import dataclass

def create(network:str,freeze:str,heating:str,bluescreen:str,osslow:str):
    new_problem= Problem(
       network=network,
       freeze=freeze,
       heating=heating,
       bluescreen=bluescreen,
       osslow=osslow
    )
    dataclass.create(new_problem)
