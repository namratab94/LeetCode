'''
Problem Number: 442
Difficulty level: Medium
Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
Author: namratabilurkar
'''

'''
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''

from collections import Counter as c

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(c(nums) - c(set(nums)))


output = Solution()
print(output.findDuplicates(nums=[4,3,2,7,8,2,3,1])) # [2,3]