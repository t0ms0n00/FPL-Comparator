from apis.fplAPI import *
from apis.videoAPI import *


class Parser:

    def __init__(self, data):
        self.player1Data = {}
        self.player2Data = {}
        self.team1 = data['team1']
        self.team2 = data['team2']
        self.player1ID = data['player1']
        self.player2ID = data['player2']
        self.fromGW = int(data['from_gw'])
        self.toGW = data['to_gw']
        self.extras = True if data['extras'] is not None else False

        self.innerHTML = ''

        self.playersAPIHandler = FplAPIPlayersHandler()
        self.player1DetailsHandler = FplAPIPlayerDetailsHandler(self.player1ID)
        self.player2DetailsHandler = FplAPIPlayerDetailsHandler(self.player2ID)
        self.fixturesHandler = FplAPIFixturesHandler(self.toGW + 1)
        self.plHighlightsHandler = PLVideoAPI()

    def parse(self):
        self.playerDetailsParse()
        if self.extras:
            self.getNextGWFixtures()
            self.getHighlights()
        return self.player1Data, self.player2Data, self.innerHTML

    def playerDetailsParse(self):
        self.player1Data['Name'] = self.getNameByID(self.player1ID)
        self.player2Data['Name'] = self.getNameByID(self.player2ID)
        self.player1Data.update(self.player1DetailsHandler.getPlayerStats(self.fromGW, self.toGW))
        self.player2Data.update(self.player2DetailsHandler.getPlayerStats(self.fromGW, self.toGW))

    def getNameByID(self, id):
        return self.playersAPIHandler.getNameByID(id)

    def getNextGWFixtures(self):
        fixtures1 = self.fixturesHandler.getNextFixture(self.team1)
        fixtures2 = self.fixturesHandler.getNextFixture(self.team2)
        fix1Formatted = ''
        fix2Formatted = ''
        for fixture in fixtures1:
            home, away = str(fixture[0]), str(fixture[1])
            if home == self.team1:
                fix1Formatted += self.playersAPIHandler.getTeamShortnameByID(away).upper()
            else:
                fix1Formatted += self.playersAPIHandler.getTeamShortnameByID(home).lower()
            fix1Formatted += ' '
        for fixture in fixtures2:
            home, away = str(fixture[0]), str(fixture[1])
            if home == self.team2:
                fix2Formatted += self.playersAPIHandler.getTeamShortnameByID(away).upper()
            else:
                fix2Formatted += self.playersAPIHandler.getTeamShortnameByID(home).lower()
            fix2Formatted += ' '
        self.player1Data['Next GW'] = fix1Formatted
        self.player2Data['Next GW'] = fix2Formatted

    def getHighlights(self):
        h1 = self.plHighlightsHandler.getHighlights(self.playersAPIHandler.getTeamNameByID(self.team1))
        h2 = self.plHighlightsHandler.getHighlights(self.playersAPIHandler.getTeamNameByID(self.team2))
        for element in h1:
            self.innerHTML += element
        for element in h2:
            self.innerHTML += element
        self.innerHTML = 'Highlights: <br> ' + self.innerHTML
