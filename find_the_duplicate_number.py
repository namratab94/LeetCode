'''
Problem Number: 287
Difficulty level: Medium
Link: https://leetcode.com/problems/find-the-duplicate-number/description/
Author: namratabilurkar
'''
'''
Input: [2,2,1]
Output: 2

Input: [4,1,1,3,2]
Output: 1
'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_len = len(set(nums))
        actual_len = len(nums)

        unique_sum = sum(set(nums))
        actual_sum = sum(nums)

        repeated_num = (actual_sum - unique_sum) // (actual_len - unique_len)

        return repeated_num



# op1 = 2
op1 = 1
# nums = [2,2,1]
# nums = [1,1]
nums = [4,1,1,3,2]
output = Solution()
print(output.findDuplicate(nums) == op1)