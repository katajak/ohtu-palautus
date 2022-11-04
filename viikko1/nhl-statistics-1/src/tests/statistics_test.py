import unittest
from statistics import Statistics, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search(self):
        self.assertEqual(str(self.statistics.search("Kurri")), "Kurri EDM 37 + 53 = 90")
        self.assertEqual(self.statistics.search("Nobody"), None)

    def test_team(self):
        players_of_team = self.statistics.team("EDM")
        i = 1
        for player in players_of_team:
            if i == 1:
                self.assertEqual(str(player), "Semenko EDM 4 + 12 = 16")
            elif i == 2:
                self.assertEqual(str(player), "Kurri EDM 37 + 53 = 90")
            elif i == 3:
                self.assertEqual(str(player), "Gretzky EDM 35 + 89 = 124")
            i += 1

    def test_invalid_team(self):
        self.assertEqual(self.statistics.team("AAA"), [])

    def test_top_points(self):
        top_3 = self.statistics.top(3, SortBy.POINTS)
        i = 1
        for player in top_3:
            if i == 1:
                self.assertEqual(str(player), "Gretzky EDM 35 + 89 = 124")
            elif i == 2:
                self.assertEqual(str(player), "Lemieux PIT 45 + 54 = 99")
            elif i == 3:
                self.assertEqual(str(player), "Yzerman DET 42 + 56 = 98")
            i += 1
    
    def test_top_goals(self):
        top_3 = self.statistics.top(3, SortBy.GOALS)
        i = 1
        for player in top_3:
            if i == 1:
                self.assertEqual(str(player), "Lemieux PIT 45 + 54 = 99")
            elif i == 2:
                self.assertEqual(str(player), "Yzerman DET 42 + 56 = 98")
            elif i == 3:
                self.assertEqual(str(player), "Kurri EDM 37 + 53 = 90")
            i += 1

    def test_assists(self):
        top_3 = self.statistics.top(3, SortBy.ASSISTS)
        i = 1
        for player in top_3:
            if i == 1:
                self.assertEqual(str(player), "Gretzky EDM 35 + 89 = 124")
            elif i == 2:
                self.assertEqual(str(player), "Yzerman DET 42 + 56 = 98")
            elif i == 3:
                self.assertEqual(str(player), "Lemieux PIT 45 + 54 = 99")
            i += 1