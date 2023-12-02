import itertools


with open("2023/day_2/part_1/input.txt", "r") as f:
    lines = f.readlines()

limits = {"red": 12, "green": 13, "blue": 14}


def key(num_colour):
    num_colour[1]  # Return the colour


games = {
    int(game.split()[-1]): {
        colour: max([int(n) for n, c in group])
        for colour, group in itertools.groupby(
            sorted(
                [
                    num_colour.split()
                    for num_colour in cubes.replace("; ", ", ").split(", ")
                ],
                key=key,
            ),
            key=key,
        )
    }
    for game, cubes in [line.replace("\n", "").split(": ") for line in lines]
}

possible = [
    game_id
    for game_id, max_cubes in games.items()
    if all([max_cubes.get(colour, 0) <= limit for colour, limit in limits.items()])
]

print(f"The sum of the IDs of the games with the specified limits is: {sum(possible)}")
