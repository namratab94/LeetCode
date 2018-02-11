'''
Problem Number: 242
Difficulty level: Easy
Link: https://leetcode.com/problems/valid-anagram/
'''

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        # Loop to add each character of 
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
                
        for i in t:
            if i not in dict:
                return False
            else:
                dict[i] -= 1
        
        for i in dict:
            if dict[i] != 0:
                return False
        return True


s = "abc"
t = "bac"
op = isAnagram(s, t)
print(op)