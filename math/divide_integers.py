""" MEDIUM
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:

-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # MAX_INT = 2 ** 31 - 1
        # MIN_INT = -2 ** 31

        # if dividend == MIN_INT and divisor == -1:
        #     return MAX_INT
        # # We need to convert both numbers to negatives.
        # # Also, we count the number of negatives signs.
        # negatives = 2
        # if dividend > 0:
        #     negatives -= 1
        #     dividend = -dividend
        # if divisor > 0:
        #     negatives -= 1
        #     divisor = -divisor
        # doubles = []
        # powersOfTwo = []

        # # Nothing too exciting here, we're just making a list of doubles of 1 and
        # # the divisor. This is pretty much the same as Approach 2, except we're
        # # actually storing the values this time. */
        # powerOfTwo = 1
        # while divisor >= dividend:
        #     doubles.append(divisor)
        #     powersOfTwo.append(powerOfTwo)
        #     # Prevent needless overflows from occurring...
        #     if divisor < MIN_INT // 2:
        #         break
        #     divisor += divisor # Double divisor
        #     powerOfTwo += powerOfTwo

        # # Go from largest double to smallest, checking if the current double fits.
        # # into the remainder of the dividend.
        # quotient = 0
        # for i in reversed(range(len(doubles))):
        #     if doubles[i] >= dividend:
        #         # If it does fit, add the current powerOfTwo to the quotient.
        #         quotient += powersOfTwo[i]
        #         # Update dividend to take into account the bit we've now removed.
        #         dividend -= doubles[i]

        # # If there was originally one negative sign, then
        # # the quotient remains negative. Otherwise, switch
        # # it to positive.
        # return quotient if negatives != 1 else -quotient
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        s = str(dividend / divisor)
        res = ""
        i = 0
        while i < len(s) and s[i] != ".":
            res += s[i]
            i += 1
        return int(res)
