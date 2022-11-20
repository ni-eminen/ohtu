from player_stats import PlayerStats
from player_reader import PlayerReader

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    pr = PlayerReader(url)
    pr.get_players()
    stats = PlayerStats(pr)
    players = stats.top_scorers_by_nationality('USA')

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
