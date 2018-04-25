'''
Problem Number: 389
Difficulty level: Easy
Link: https://leetcode.com/problems/find-the-difference
Author: namratabilurkar
'''

'''
Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
'''


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t = list(t)
        s = list(s)
        for c in s:
            t.remove(c)
        return t[0]


# s = "abcd"
s = "a"
# t = "abcde"
t = "aa"
output = Solution()
print(output.findTheDifference(s,t)) # 'a' is the expected solution