'''
Problem Number: 268
Difficulty level: Easy
Link: https://leetcode.com/problems/missing-number/description/
Author: namratabilurkar
'''

'''
Input: [3,0,1]
Output: 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expected_total = -1
        actual_total = 0
        total = 0

        for i in range(0, len(nums)+1):
            if i < len(nums):
                actual_total += nums[i]
            expected_total += 1
            total += expected_total
        return total - actual_total


nums = [3,0,1] # O/P: 2
# nums = [9,6,4,2,3,5,7,0,1] # O/P: 8

output = Solution()
print(output.missingNumber(nums))