"""
989. Add to Array-Form of Integer
Easy
Topics
Companies
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

Constraints:

1 <= num.length <= 10^4
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 10^4
"""


class Solution:
    def solve(self, num: [int], k: int) -> [int]:
        # O(n) time, O(n) space
        res = []
        carry = k

        # iterate backwards
        for i in range(len(num) - 1, -1, -1):
            total = carry
            if num[i] > 0:
                total += num[i]
            if total >= 10:
                carry = int(total / 10)
                res.append(total % 10)
            else:
                carry = 0
                res.append(total)
        while carry > 0:
            res.append(carry % 10)
            carry = int(carry / 10)
        res.reverse()
        return res
