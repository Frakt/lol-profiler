#DataBase Manager import
import lolprofiler_dbm
#RiotWatcher Imports
from riotwatcher import RiotWatcher,EUROPE_WEST

#CONSTANTS
SQUIRELS_ID = 'TEAM-4582d4b0-24da-11e4-958e-c81f66db96d8'

#RiotWatcher Init(BiggyFr Key + EUW as Default Region)
rw = RiotWatcher('79531c6e-3aaf-4e83-9f5d-61ac8c4c5982', default_region=EUROPE_WEST)

#lolprofiler_dbm.createdb()

def get_team_matchId_history_from_riot(team_id):
    team = rw.get_team(team_id)
    history = team['matchHistory']
    matchId = []
    for match in history:
        matchId.append(match['gameId'])
    return matchId

def get_match(matchId):
    match = rw.get_match(matchId)
    return match

matchId = get_team_matchId_history_from_riot(SQUIRELS_ID)
print(get_match(matchId[0]))
