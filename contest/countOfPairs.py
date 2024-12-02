"""
You are given three positive integers n, x, and y.

In a city, there exist houses numbered 1 to n connected by n streets. There is a street connecting the house numbered i with the house numbered i + 1 for all 1 <= i <= n - 1 . An additional street connects the house numbered x with the house numbered y.

For each k, such that 1 <= k <= n, you need to find the number of pairs of houses (house1, house2) such that the minimum number of streets that need to be traveled to reach house2 from house1 is k.

Return a 1-indexed array result of length n where result[k] represents the total number of pairs of houses such that the minimum streets required to reach one house from the other is k.

Note that x and y can be equal.

example:
Input: n = 3, x = 1, y = 3
Output: [6,0,0]
Explanation: Let's look at each pair of houses:
- For the pair (1, 2), we can go from house 1 to house 2 directly.
- For the pair (2, 1), we can go from house 2 to house 1 directly.
- For the pair (1, 3), we can go from house 1 to house 3 directly.
- For the pair (3, 1), we can go from house 3 to house 1 directly.
- For the pair (2, 3), we can go from house 2 to house 3 directly.
- For the pair (3, 2), we can go from house 3 to house 2 directly.

example:
Input: n = 5, x = 2, y = 4
Output: [10,8,2,0,0]
Explanation: For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (2, 4), (4, 2), (3, 4), (4, 3), (4, 5), and (5, 4).
- For k == 2, the pairs are (1, 3), (3, 1), (1, 4), (4, 1), (2, 5), (5, 2), (3, 5), and (5, 3).
- For k == 3, the pairs are (1, 5), and (5, 1).
- For k == 4 and k == 5, there are no pairs.

example:
Input: n = 4, x = 1, y = 1
Output: [6,4,2,0]
Explanation: For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (3, 4), and (4, 3).
- For k == 2, the pairs are (1, 3), (3, 1), (2, 4), and (4, 2).
- For k == 3, the pairs are (1, 4), and (4, 1).
- For k == 4, there are no pairs.

Constraints:

2 <= n <= 100
1 <= x, y <= n
"""

"""Solution

To solve this problem, we need to calculate the number of pairs of houses (house1, house2) for each possible minimum number of streets k that must be traveled to go from house1 to house2. The city has n houses and a special street that directly connects house x with house y.

The key to solving this problem is understanding how the addition of the street between house x and house y affects the minimum distance between different pairs of houses. We can break this down into a few steps:

Calculate Distances without the Special Street: For each pair of houses (i, j), the minimum distance without considering the special street is simply abs(i - j).

Calculate Distances with the Special Street: The special street potentially shortens the distance between some pairs of houses. To calculate the distance considering the special street, we must consider the distance going through the special street, which is abs(x - i) + 1 + abs(y - j) or abs(y - i) + 1 + abs(x - j).

Count Pairs for Each Distance: For each possible distance k (from 1 to n), count the number of pairs (i, j) where the minimum of the two calculated distances (with and without the special street) is k.

Return the Count for Each Distance: Store the counts in an array indexed by the distance k.
"""


def countOfPairs(n, x, y):
    result = [0] * n

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # Calculate distance without the special street
            direct_distance = j - i

            # Calculate distance with the special street
            special_street_distance = min(
                abs(x - i) + 1 + abs(y - j), abs(y - i) + 1 + abs(x - j)
            )

            # Find the minimum of the two distances
            min_distance = min(direct_distance, special_street_distance)

            # Count this pair for the corresponding distance
            if min_distance <= n:
                result[min_distance - 1] += 1

    # Each pair is counted twice (i, j) and (j, i)
    result = [count * 2 for count in result]

    return result
