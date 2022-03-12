import json
from math import inf

import requests


class FplAPIPlayersHandler:

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

    def getNameByID(self, id):
        req = requests.get(self.generalURL)
        playersList = json.loads(req.content)['elements']
        name = [x['web_name'] + ' ' + x['first_name'] for x in playersList if x['id'] == int(id)]
        return name[0]


class FplAPIGWHandler:

    def __init__(self):
        self.generalURL = 'https://fantasy.premierleague.com/api/bootstrap-static/'

    def getFinishedGW(self):
        req = requests.get(self.generalURL)
        eventsList = json.loads(req.content)['events']
        finished = max([event['id'] for event in eventsList if event['finished'] is True])
        return finished


class FplAPIPlayerDetailsHandler:

    def __init__(self, playerID):
        self.generalURL = 'https://fantasy.premierleague.com/api/element-summary/' + playerID + '/'
        self.goals = None
        self.assists = None
        self.cs = None
        self.gc = None
        self.yc = None
        self.rc = None
        self.minutes = None

    def getPlayerGoals(self, fromGW, toGW):
        req = requests.get(self.generalURL)
        data = json.loads(req.content)['history']
        goalsList = [el['goals_scored'] for el in data if fromGW <= el['round'] <= toGW]
        self.goals = sum(goalsList)
        return self.goals

    def getPlayerAssists(self, fromGW, toGW):
        req = requests.get(self.generalURL)
        data = json.loads(req.content)['history']
        assistsList = [el['assists'] for el in data if fromGW <= el['round'] <= toGW]
        self.assists = sum(assistsList)
        return self.assists

    def getPlayerCS(self, fromGW, toGW):
        req = requests.get(self.generalURL)
        data = json.loads(req.content)['history']
        csList = [el['clean_sheets'] for el in data if fromGW <= el['round'] <= toGW]
        self.cs = sum(csList)
        return self.cs

    def getPlayerGC(self, fromGW, toGW):
        req = requests.get(self.generalURL)
        data = json.loads(req.content)['history']
        gcList = [el['goals_conceded'] for el in data if fromGW <= el['round'] <= toGW]
        self.gc = sum(gcList)
        return self.gc

    def getPlayerYC(self, fromGW, toGW):
        req = requests.get(self.generalURL)
        data = json.loads(req.content)['history']
        ycList = [el['yellow_cards'] for el in data if fromGW <= el['round'] <= toGW]
        self.yc = sum(ycList)
        return self.yc

    def getPlayerRC(self, fromGW, toGW):
        req = requests.get(self.generalURL)
        data = json.loads(req.content)['history']
        rcList = [el['red_cards'] for el in data if fromGW <= el['round'] <= toGW]
        self.rc = sum(rcList)
        return self.rc

    def getPlayerMinutes(self, fromGW, toGW):
        req = requests.get(self.generalURL)
        data = json.loads(req.content)['history']
        minutesPerMatch = [el['minutes'] for el in data if fromGW <= el['round'] <= toGW]
        self.minutes = sum(minutesPerMatch)
        return self.minutes

    def getMinutesPerGoal(self):
        if self.goals == 0:
            return inf
        return round(self.minutes/self.goals, 2)
