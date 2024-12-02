"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 231 - 1
"""

# Similar to next permutation problem


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Convert the input string to a list of characters
        arr = list(str(n))
        n = len(arr)
        i = n - 2

        # Find the largest index i such that arr[i] < arr[i+1]
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        # If no such index exists, return -1
        if i < 0:
            return -1
        j = n - 1

        # Find the largest index j such that arr[i] < arr[j]
        while j >= 0 and arr[j] <= arr[i]:
            j -= 1
        # Swap arr[i] and arr[j]
        arr[i], arr[j] = arr[j], arr[i]

        # Function to reverse the array
        def rev(arr: list, start: int, end: int) -> None:
            while start < end:
                swap(arr, start, end)
                start += 1
                end -= 1

        # Function to swap two numbers
        def swap(arr: list, i: int, j: int) -> None:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        # Reverse the sublist arr[start:end+1]
        rev(arr, i + 1, n - 1)

        if int("".join(arr)) > 2**31 - 1:  # larger than the constraints
            return -1

        return int("".join(arr))
