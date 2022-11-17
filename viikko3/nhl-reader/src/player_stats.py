def sort_by_points(player):
    return player.points

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players(nationality)
        players.sort(reverse=True, key=sort_by_points)
        print(f"Players from {nationality}:\n")
        return players
