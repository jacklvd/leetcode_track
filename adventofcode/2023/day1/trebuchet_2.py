"""
--- Part Two ---
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""
# Python Imports

import re

from pathlib import Path


def load_data(path):
    """Return generator of (whitespace-stripped) lines from input."""
    with path.open() as ifh:
        return (_.strip() for _ in ifh.readlines())


digre = re.compile(
    "0|1|2|3|4|5|6|7|8|9|zer(?=)o|on(?=e)|tw(?=o)|thre(?=e)|four|fiv(?=e)|six|seve(?=n)|eigh(?=t)|nin(?=e)"
)

digdict = {
    "zero": "0",
    "on": "1",
    "tw": "2",
    "thre": "3",
    "four": "4",
    "fiv": "5",
    "six": "6",
    "seve": "7",
    "eigh": "8",
    "nin": "9",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def parse_data(data):
    """Return list of integers made from of first and last digit in each line."""
    vals = []
    for line in data:
        diglist = []  # ordered list of positions of digits
        for match in re.finditer(digre, line):
            diglist.append((match.start(), digdict[match.group()]))
        vals.append(diglist[0][1] + diglist[-1][1])
        print(vals)
    return [int(_) for _ in vals]


data = load_data(Path("input2.txt"))
vals = parse_data(data)
print(sum(vals))
