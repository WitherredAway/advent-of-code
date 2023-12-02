import itertools


with open("2023/day_2/part_1/input.txt", "r") as f:
    lines = f.readlines()

limits = {"red": 12, "green": 13, "blue": 14}


def key(num_colour):
    return num_colour[1]  # Return the colour


# shenanigans
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
    [x := 1, [x := x * i for i in max_cubes.values()]][-1][-1]  # prod using list comprehension, thanks oli
    for max_cubes in games.values()
]

print(f"The sum of the IDs of the games with the specified limits is: {sum(possible)}")
