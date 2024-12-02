"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
"""


class Solution:
    def solve(nums: [int]) -> [int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        freq_tuples = [(freq[num], -num, num) for num in nums]

        for i in range(len(freq_tuples)):
            for j in range(len(freq_tuples) - i - 1):
                if freq_tuples[j] > freq_tuples[j + 1]:
                    freq_tuples[j], freq_tuples[j + 1] = (
                        freq_tuples[j + 1],
                        freq_tuples[j],
                    )

        # Reconstruct the sorted list based on the sorted tuples
        sorted_nums = [tup[2] for tup in freq_tuples]

        return sorted_nums
