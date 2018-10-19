'''
Problem Number: 561
Difficulty level: Easy
Link: https://leetcode.com/problems/array-partition-i/
Author: namratabilurkar
'''

'''
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

'''

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)

        pairs_sum = 0
        for i in range(0, len(nums) - 1, 2):
            temp_sum = min(nums[i], nums[i + 1])
            pairs_sum += temp_sum
        return pairs_sum