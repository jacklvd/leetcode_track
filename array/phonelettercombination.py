"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def uniq_combine(num, n, table):
            if not num:
                return ""
            lst = []
            q = deque()
            q.append("")

            while len(q) != 0:
                s = q.pop()

                # If complete word is generated
                # push it in the list
                if len(s) == n:
                    lst.append(s)
                else:
                    # Try all possible letters for current digit
                    # in number[]
                    for letter in table[num[len(s)]]:
                        q.append(s + letter)

            # Return the generated list
            return lst

        res = []
        number = [int(i) for i in list(digits)]

        combinations = uniq_combine(number, len(digits), table)
        for word in combinations:
            res.append(word)
        return res
