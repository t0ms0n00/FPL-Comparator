import json
import requests


class FplAPI:
    def __init__(self):
        self.generalURL = 'https://fantasy.premierleague.com/api/bootstrap-static/'

    def getTeams(self):
        req = requests.get(self.generalURL)
        teams = json.loads(req.content)['teams']
        teams_data = [(team['id'], team['name']) for team in teams]
        return teams_data

    def getPlayersFromTeam(self, teamID):
        req = requests.get(self.generalURL)
        playersList = json.loads(req.content)['elements']
        teamPlayers = [(x['id'], x['web_name'] + ' ' + x['first_name']) for x in playersList if x['team'] == int(teamID)]
        return teamPlayers
