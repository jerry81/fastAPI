from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from models import Player, Team
from schemas import TeamCreate, PlayerCreate


def get_player(db: Session, player_id: int):
    return db.query(Player).filter(models.Player.id == player_id).first()


def get_player_by_name(db: Session, name: str):
    return db.query(Player).filter(models.Player.name == name).first()


def get_players(db: Session, skip: int = 0, limit: int = 100):
    players = db.query(Player).offset(skip).limit(limit).all()
    print("players is ", players)
    return players


def create_player(db: Session, player: PlayerCreate):
    db_player = Player(name=player.name, height=player.height, active=player.active, position=player.position)
    print("i am here", db_player)            
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Team).offset(skip).limit(limit).all()

def create_team(db: Session, team: TeamCreate):
    db_team = Team(name=team.name, city=team.city)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team
