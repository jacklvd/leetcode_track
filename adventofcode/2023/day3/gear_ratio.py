"""
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""


def parse_schematic(schematic):
    """Parse the schematic into a 2D array."""
    return [list(line) for line in schematic.strip().split("\n")]


def is_adjacent_to_symbol(schematic, row, col):
    """Check if the position is adjacent to any symbol other than '.'"""
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if (
            0 <= r < len(schematic)
            and 0 <= c < len(schematic[0])
            and schematic[r][c] not in ".0123456789"
        ):
            return True
    return False


def sum_part_numbers(schematic):
    """Calculate the sum of all part numbers."""
    schematic = parse_schematic(schematic)
    total = 0
    row = 0
    while row < len(schematic):
        col = 0
        while col < len(schematic[row]):
            if schematic[row][col].isdigit():
                number = ""
                while col < len(schematic[row]) and schematic[row][col].isdigit():
                    number += schematic[row][col]
                    col += 1
                if is_adjacent_to_symbol(schematic, row, col - len(number)):
                    total += int(number)
            else:
                col += 1
        row += 1
    return total


# Example usage
schematic_example = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
print(sum_part_numbers(schematic_example))
