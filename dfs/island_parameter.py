"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
"""


# first solution not using dfs
def islandPerimeter(grid):
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter


# using dfs
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited = set([(i, j)])
                    self.dfs(grid, i, j, visited)
                    return self.total
        return 0

    def dfs(self, grid, i, j, visited):
        edges = 4
        for del_i, del_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_i, next_j = i + del_i, j + del_j
            if (
                0 <= next_i < len(grid)
                and 0 <= next_j < len(grid[0])
                and grid[next_i][next_j] == 1
            ):
                edges -= 1
                if (next_i, next_j) not in visited:
                    visited.add((next_i, next_j))
                    self.dfs(grid, next_i, next_j, visited)
        self.total += edges
