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
        self.points = None

    def getPlayerStats(self, fromGW, toGW):
        stats = {}

        req = requests.get(self.generalURL)
        dataHistory = json.loads(req.content)['history']

        goalsList = [el['goals_scored'] for el in dataHistory if fromGW <= el['round'] <= toGW]
        assistsList = [el['assists'] for el in dataHistory if fromGW <= el['round'] <= toGW]
        csList = [el['clean_sheets'] for el in dataHistory if fromGW <= el['round'] <= toGW]
        gcList = [el['goals_conceded'] for el in dataHistory if fromGW <= el['round'] <= toGW]
        ycList = [el['yellow_cards'] for el in dataHistory if fromGW <= el['round'] <= toGW]
        rcList = [el['red_cards'] for el in dataHistory if fromGW <= el['round'] <= toGW]
        minutesPerMatch = [el['minutes'] for el in dataHistory if fromGW <= el['round'] <= toGW]
        points = [el['total_points'] for el in dataHistory if fromGW <= el['round'] <= toGW]

        self.goals = sum(goalsList)
        self.assists = sum(assistsList)
        self.cs = sum(csList)
        self.gc = sum(gcList)
        self.yc = sum(ycList)
        self.rc = sum(rcList)
        self.minutes = sum(minutesPerMatch)
        self.points = sum(points)

        stats['Goals'] = self.goals
        stats['Assists'] = self.assists
        stats['Goals conceded'] = self.gc
        stats['Clean sheets'] = self.cs
        stats['Yellow cards'] = self.yc
        stats['Red cards'] = self.rc
        stats['Minutes'] = self.minutes
        stats['Minutes per goal'] = self.getMinutesPerGoal()
        stats['Points'] = self.points
        stats['Form (PPG)'] = self.getPointsPerGame(fromGW, toGW)

        return stats

    def getMinutesPerGoal(self):
        if self.goals == 0:
            return inf
        return round(self.minutes/self.goals, 2)

    def getPointsPerGame(self, fromGw, toGw):
        return round(self.points/(toGw-fromGw+1), 1)
