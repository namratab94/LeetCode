'''
Problem Number: 344
Difficulty level: Easy
Link: https://leetcode.com/problems/reverse-string/description/
Author: namratabilurkar
'''

'''
Input:
s = "hello"

Output:
"olleh"

'''


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return s[::-1]
        mid_index = len(s) / 2
        start = 0
        end = len(s) - 1
        s = list(s)
        while (start < mid_index):
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        return "".join(s)