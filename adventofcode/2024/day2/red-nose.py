"""
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
"""


def read_file_to_2d_list(file_path):
    """
    Reads a text file and creates a 2D list where each row in the file
    becomes a list in the 2D list.

    Args:
        file_path (str): Path to the input text file.

    Returns:
        list: A 2D list with integers from the file.
    """
    data_2d_list = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                # Split the line into numbers and convert them to integers
                row = [int(num) for num in line.split()]
                data_2d_list.append(row)
        return data_2d_list
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


# Example usage:
file_path = "input.txt"  # Replace with the path to your file
data = read_file_to_2d_list(file_path)

# print("2D List:")
# for row in data:
#     print(row)

total = 0


# check if all increasing and different by 1, 2, or 3
def is_safe(row):
    for i in range(1, len(row)):
        if row[i] - row[i - 1] not in {1, 2, 3} or row[i - 1] > row[i]:
            return False
    return True


# check if all decreasing and different by 1, 2, or 3
def is_safe_decreasing(row):
    for i in range(1, len(row)):
        if row[i - 1] - row[i] not in {1, 2, 3} or row[i - 1] < row[i]:
            return False
    return True


for row in data:
    if is_safe(row) or is_safe_decreasing(row):
        total += 1
# print(total)

"""
--- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""


def is_safe_record(report: list[int], allow_removal=False) -> bool:
    ascending = report[1] > report[0]

    is_safe = True

    for i in range(1, len(report)):
        a, b = report[i], report[i - 1]
        if (a > b) != ascending or abs(a - b) > 3 or a == b:
            is_safe = False

    if not is_safe and allow_removal:
        for i in range(len(report)):
            if is_safe_record(report[0:i] + report[i + 1 :]):
                is_safe = True

    return is_safe


total = 0
for row in data:
    if is_safe_record(row, True):
        total += 1
print(total)
