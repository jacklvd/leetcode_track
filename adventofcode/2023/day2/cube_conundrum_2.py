"""
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present.
"""
with open("input2.txt", "r") as file:
    input_data = file.read()

# Split the input data into individual games
games = input_data.split("\n")


# Function to find the minimum number of cubes for each color in a game
def find_minimum_cubes(game):
    color_counts = game.split(":")[1].split(";")
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for count in color_counts:
        items = count.split(",")
        for item in items:
            parts = item.strip().split(" ")
            number = int(parts[0])
            color = parts[1]
            min_cubes[color] = max(min_cubes[color], number)
    return min_cubes


# Function to calculate the power of a set of cubes
def calculate_power(cubes):
    return cubes["red"] * cubes["green"] * cubes["blue"]


# Initialize a variable to store the sum of the powers
total_power = 0

# Calculate the minimum number of cubes and their power for each game
for game in games:
    min_cubes = find_minimum_cubes(game)
    power = calculate_power(min_cubes)
    total_power += power

# Print the result
print("Total power of all games:", total_power)
