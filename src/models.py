from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

print('building on base')
class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True, index=True)
    position = Column(String(1))
    height = Column(Integer)
    active = Column(Boolean, default=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="players")
    
class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True, index=True)
    city = Column(String(20))
    players = relationship("Player", back_populates="teams")