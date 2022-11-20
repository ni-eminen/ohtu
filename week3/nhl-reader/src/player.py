class Player:
    def __init__(self, player):
        self.player = player
        #self.name, self.nationality, self.assists, self.goals, self.penalties, self.team, self.games = player['name'], \
        #    player['nationality'], player['assists'], player['goals'], player['penalties'], player['team'],\
        #    player['games']

    def __str__(self):
        str = ''
        for key in self.player:
            str += key + ' ' if key == 'goals' or key == 'assists' else ''
            str += f'{self.player[key]:20} ' if key == 'name' else f'{self.player[key].__str__()} '

        return str

    def get_nationality(self):
        return self.player['nationality']
    def get_goals(self):
        return self.player['goals']