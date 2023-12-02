with open("2023/day_2/part_1/input.txt", "r") as f:
    lines = f.readlines()

games = {
    int(game.split()[-1]): [
        {
            colour: int(num)
            for num, colour in [num_colour.split() for num_colour in _set.split(", ")]
        }
        for _set in cubes.split("; ")
    ]
    for game, cubes in [line.replace("\n", "").split(": ") for line in lines]
}

limits = {"red": 12, "green": 13, "blue": 14}

possible = [
    game_id
    for game_id, cubes in games.items()
    if all(
        [
            max([_set.get(colour, 0) for _set in cubes]) < limit
            for colour, limit in limits.items()
        ]
    )
]
print(sum(possible))
