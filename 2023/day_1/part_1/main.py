with open("2023/day_1/part_1/input.txt", "r") as f:
    lines = f.readlines()

# i am mentally deranged
answer = sum(
    [int((f := [l for l in line if l.isdigit()])[0] + f[-1]) for line in lines]
)
print(f"The sum of all of the calibration values is {answer}")
