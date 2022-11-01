import unittest

from player_reader import PlayerReader
from player import Player
from statistics import Statistics
from constants import SortBy


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
        p = self.statistics.search('Semenko')
        self.assertEqual(p.name, 'Semenko')

        p = self.statistics.search('asdfasfasfdsaf Fogarty')
        self.assertEqual(p, None)

    def test_top(self):
        p = self.statistics.top(3, SortBy.POINTS)
        self.assertEqual(p != None, True)
        p = self.statistics.top(3, SortBy.ASSISTS)
        self.assertEqual(p != None, True)
        p = self.statistics.top(3, SortBy.GOALS)
        self.assertEqual(p != None, True)

    def test_team(self):
        team = self.statistics.team('EDM')
        self.assertEqual(len(team) > 0, True)
