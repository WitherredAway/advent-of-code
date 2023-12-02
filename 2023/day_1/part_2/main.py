with open("2023/day_1/part_2/input.txt", "r") as f:
    inp = f.read()
    for digit, word in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        inp = inp.replace(word, f"{word[:len(word)//2]}{digit}{word[len(word)//2:]}")
    lines = inp.split("\n")

# i am mentally deranged
answer = sum(
    [int(f[0] + f[-1]) for line in lines if (f := [l for l in line if l.isdigit()])]
)
print(f"The sum of all of the calibration values with spelled out digits is {answer}")
