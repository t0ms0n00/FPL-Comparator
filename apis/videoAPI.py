import json
import requests


class PLVideoAPI:

    def __init__(self):
        self.address = 'https://www.scorebat.com/video-api/v3/feed/?token='
        self.token = 'MTU0MjFfMTY0NzE2NTg5MV8zNzQ0YmNhMTg2ZjBlMjAxMTIyOWM2OTgyNjdlNjQwZWEzYmQ0ZWUy'
        self.nameMap = {
            'Arsenal': 'Arsenal',
            'Aston Villa': 'Aston Villa',
            'Brentford': 'Brentford',
            'Brighton': 'Brighton',
            'Burnley': 'Burnley',
            'Chelsea': 'Chelsea',
            'Crystal Palace': 'Crystal Palace',
            'Everton': 'Everton',
            'Leicester': 'Leicester',
            'Leeds': 'Leeds',   # check
            'Liverpool': 'Liverpool',
            'Man City': 'Manchester City',
            'Man Utd': 'Manchester United',
            'Newcastle': 'Newcastle',
            'Norwich': 'Norwich',
            'Southampton': 'Southampton', #check
            'Spurs': 'Tottenham Hotspur',
            'Watford': 'Watford',
            'West Ham': 'West Ham',
            'Wolves': 'Wolves' #check
        }

    def getHighlights(self, teamName):
        url = self.address+self.token
        req = requests.get(url)
        objects = json.loads(req.content)['response']
        videos = []
        name = self.nameMap.get(teamName, '')
        for el in objects:
            if name in el['title']:
                videos += el['videos']
        embed = [video['embed'] for video in videos]
        return embed
