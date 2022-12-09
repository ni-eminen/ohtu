from src.QueryBuilder import QueryBuilder
from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )


    matcher = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )

    matcher = All()

    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    query = QueryBuilder()
    m1 = (
        query
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    m2 = (
        query
        .playsIn("EDM")
        .hasAtLeast(50, "points")
        .build()
    )

    matcher = (
        query
        .oneOf(
            query.playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build(),
            query.playsIn("EDM")
            .hasAtLeast(50, "points")
            .build()
        )
        .build()
    )

    print_with_matcher(matcher, stats)


def print_with_matcher(matcher, stats):
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
