"""
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""

# A monotonic stack problem

"""
Approach:
1. Use a stack to store the index of the elements in nums.
2. Iterate through nums twice, the second time is to simulate the circular array.
3. For each element in nums, pop out the smaller elements in the stack, and update the result array.
4. Push the current element into the stack.
5. Return the result array.
"""


class Solution:
    def nextGreaterElements(self, nums: [int]) -> [int]:
        n = len(nums)
        stack = []
        res = [-1] * n
        for i in range(n * 2, 0, -1):
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()
            res[i % n] = -1 if not stack else nums[stack[-1]]
            stack.append(i % n)
        return res
