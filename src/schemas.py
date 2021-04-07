from typing import List, Optional
from pydantic import BaseModel

class PlayerBase(BaseModel):
    name: str
    position: str
    height: int
    active: bool

class PlayerCreate(PlayerBase):
    pass 

class Player(PlayerBase):
    id: int
    team_id: int 

    class Config: 
        orm_mode = True

class TeamBase(BaseModel):
    name: str
    city: str

class TeamCreate(TeamBase):
    pass

class Team(TeamBase): 
    id: int
    players: List[Player] = []

    class Config: 
        orm_mode = True  # read data even if it is not a dict