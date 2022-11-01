from constants import SortBy
from player_reader import PlayerReader


def sort_by_(player, sort_by: SortBy):
    if sort_by is SortBy.GOALS:
        return player.goals
    elif sort_by is SortBy.POINTS:
        return player.points
    else:
        return player.assists


class Statistics:
    def __init__(self, pr: PlayerReader):
        reader = pr
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda p: sort_by_(p, sort_by)
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
