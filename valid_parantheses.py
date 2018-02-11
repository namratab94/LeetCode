'''
Problem Number: 20
Difficulty level: Easy
Link: https://leetcode.com/problems/valid-parentheses/
'''
class Solution: 
    def complement(self, b):
        if b == ')':
            return '('
        elif b == '}':
            return '{'
        else:
            return '['
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = []
        open_b = ['(', '{', '[']
        close_b = [')', '}' ']']
        s = list(s)
        for i in s:
            if i in open_b:
                d.append(i)
            else:
                if len(d) > 0:
                    if self.complement(i) != d[-1]:
                        return False
                    else:
                        d.pop()
                else:
                    return False
        if len(d) > 0:
            return False
        else:
            return True