'''
Problem number: 9
Difficulty level: Easy
Link: https://leetcode.com/problems/palindrome-number/description/
Author: namratabilurkar
'''

'''
Input: 121
Output: true

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        neg_flag = False
        num = str(x)
        if num[0] == '-':
            neg_flag = True
        
        if neg_flag:
            rev = self.reverseNumber(num[1:])
            return self.palindromeCheck(x, rev)
        else:
            rev = self.reverseNumber(num)
            return self.palindromeCheck(x, rev)
        
        
    def palindromeCheck(self, num, rev_num):
        
        if num == rev_num:
            return True
        else:
            return False
        
    def reverseNumber(self, num):
        
        # reversing the number using splicing on string
        rev_num = num[::-1]
        
        return int(rev_num)
        

output = Solution()
print(output.isPalindrome(x=121)) # True
