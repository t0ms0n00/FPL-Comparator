from apis.fplAPI import *


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
        self.odds = True if data['odds'] is not None else False

        self.playersAPIHandler = FplAPIPlayersHandler()
        self.player1DetailsHandler = FplAPIPlayerDetailsHandler(self.player1ID)
        self.player2DetailsHandler = FplAPIPlayerDetailsHandler(self.player2ID)

    def parse(self):
        self.playerDetailsParse()
        if self.odds:
            pass
            # connect next fixture fpl and then odds api
        return self.player1Data, self.player2Data

    def playerDetailsParse(self):
        self.player1Data['Name'] = self.getNameByID(self.player1ID)
        self.player2Data['Name'] = self.getNameByID(self.player2ID)
        self.player1Data['Goals'] = self.player1DetailsHandler.getPlayerGoals(self.fromGW, self.toGW)
        self.player2Data['Goals'] = self.player2DetailsHandler.getPlayerGoals(self.fromGW, self.toGW)
        self.player1Data['Assists'] = self.player1DetailsHandler.getPlayerAssists(self.fromGW, self.toGW)
        self.player2Data['Assists'] = self.player2DetailsHandler.getPlayerAssists(self.fromGW, self.toGW)
        self.player1Data['Goals conceded'] = self.player1DetailsHandler.getPlayerGC(self.fromGW, self.toGW)
        self.player2Data['Goals conceded'] = self.player2DetailsHandler.getPlayerGC(self.fromGW, self.toGW)
        self.player1Data['Clean sheets'] = self.player1DetailsHandler.getPlayerCS(self.fromGW, self.toGW)
        self.player2Data['Clean sheets'] = self.player2DetailsHandler.getPlayerCS(self.fromGW, self.toGW)
        self.player1Data['Yellow cards'] = self.player1DetailsHandler.getPlayerYC(self.fromGW, self.toGW)
        self.player2Data['Yellow cards'] = self.player2DetailsHandler.getPlayerYC(self.fromGW, self.toGW)
        self.player1Data['Red cards'] = self.player1DetailsHandler.getPlayerRC(self.fromGW, self.toGW)
        self.player2Data['Red cards'] = self.player2DetailsHandler.getPlayerRC(self.fromGW, self.toGW)
        self.player1Data['Minutes'] = self.player1DetailsHandler.getPlayerMinutes(self.fromGW, self.toGW)
        self.player2Data['Minutes'] = self.player2DetailsHandler.getPlayerMinutes(self.fromGW, self.toGW)
        self.player1Data['Minutes per goal'] = self.player1DetailsHandler.getMinutesPerGoal()
        self.player2Data['Minutes per goal'] = self.player2DetailsHandler.getMinutesPerGoal()

    def getNameByID(self, id):
        return self.playersAPIHandler.getNameByID(id)
