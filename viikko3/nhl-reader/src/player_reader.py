import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self, nationality):
        response = requests.get(self.url).json()

        players = []

        for player_dict in response:
            if player_dict["nationality"] == str(nationality):
                player = Player(
                    player_dict["name"],
                    player_dict["team"],
                    player_dict["goals"],
                    player_dict["assists"]
                )

                players.append(player)
    
        return players