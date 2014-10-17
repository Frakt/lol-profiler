#SQLAlchemy Imports
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#SQLAlchemy Init
Base = declarative_base()

class Match(Base):
    __tablename__ = 'match'
    id = Column(Integer, primary_key=True)
    matchId = Column(Integer, primary_key=True)
    matchCreation = Column(Integer)
    mapId = Column(Integer)
    season = Column(String)
    queueType = Column(String)
    matchDuration = Column(Integer)
    players = relationship('Player', secondary='stats')

class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    summonerId = Column(Integer)
    summonerName = Column(String)
    matches = relationship('Match', secondary='stats')

class Stats(Base):
    __tablename__ = 'stats'
    id = Column(Integer, primary_key=True)
    #Items
    item0 = Column(Integer)
    item1 = Column(Integer)
    item2 = Column(Integer)
    item3 = Column(Integer)
    item4 = Column(Integer)
    item5 = Column(Integer)
    item6 = Column(Integer)
    #Misc
    totalDamageDealtToChampions = Column(Integer)
    champLevel = Column(Integer)
    winner = Column(Boolean)
    championId = Column(Integer)
    #Gold
    minionsKilled = Column(Integer)
    goldEarned = Column(Integer)
    goldSpent = Column(Integer)
    #KDA
    deaths = Column(Integer)
    assists = Column(Integer)
    kills = Column(Integer)
    #Kikoo stats
    doubleKills = Column(Integer)
    tripleKills = Column(Integer)
    quadraKills = Column(Integer)
    pentaKills = Column(Integer)
    largestKillingSpree = Column(Integer)
    #Wards
    sightWardsBoughtInGame = Column(Integer)
    visionWardsBoughtInGame = Column(Integer)
    wardsPlaced = Column(Integer)
    wardsKilled = Column(Integer)
    matchId = Column(Integer, ForeignKey('match.matchId'))
    summonerId = Column(Integer, ForeignKey('player.summonerId'))

def createdb():
    engine = create_engine('sqlite:///lolprofilerdb.sqlite')
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
