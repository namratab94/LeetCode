'''
Problem Number: 32
Difficulty level: Hard
Link: https://leetcode.com/problems/longest-valid-parentheses/description/
Author: namratabilurkar
'''

'''
Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"


Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

'''
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        1. Have a stack with -1 pushed in it.
        2. If the character is '(', push it in the stack.
        3. If the character is ')', pop from the stack.
        4. If the stack is not empty, then find the maxLen using the following:
            maxLen = i - stack[len(stack)-1], else, push i in the stack.
        5. Return the maxLen
        '''
        stack = []
        stack.append(-1)
        maxLen = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()

                if stack:
                    maxLen = max(maxLen, i - stack[len(stack) - 1])
                else:
                    stack.append(i)

        return maxLen
