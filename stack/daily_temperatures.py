""" MEDIUM
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

hint:
For example, in example 1, array is[73,74,75,71,69,72,76,73]:

74 is the next largest value after 73, and 73 is a monotonic non-increasing subsequence of the original array.
72 is the next largest value after 71 and 69, and 71 and 69 form a monotonic non-increasing subsequence of the original array.

"""


# a monotonic stack problem
class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
