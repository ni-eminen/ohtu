from player_reader import PlayerReader
class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        # Get players of nationality
        ps_of_n = []
        for p in self.reader.players:
            if p.get_nationality() == nationality:
                ps_of_n.append(p)
                print(p.get_goals())
        ps_of_n.sort(key=lambda x: x.get_goals(), reverse=True)

        return ps_of_n