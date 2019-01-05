'''
Problem Number: 930
Difficulty level: Medium
Link: https://leetcode.com/problems/binary-subarrays-with-sum/
Author: namratabilurkar
'''

'''
Input: A = [1,0,1,0,1], S = 2

Output: 4

Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

'''

class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
