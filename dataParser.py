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
        self.player1Data.update(self.player1DetailsHandler.getPlayerStats(self.fromGW, self.toGW))
        self.player2Data.update(self.player2DetailsHandler.getPlayerStats(self.fromGW, self.toGW))

    def getNameByID(self, id):
        return self.playersAPIHandler.getNameByID(id)
