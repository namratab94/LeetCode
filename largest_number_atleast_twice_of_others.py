'''
Problem Number: 747
Difficulty level: Easy
Link: https://leetcode.com/problems/largest-number-at-least-twice-of-others/
Author: namratabilurkar
'''

'''
Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

'''

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = float("-inf")
        max_index = -1
        for index in range(len(nums)):
            if nums[index] > max_val:
                max_val = nums[index]
                max_index = index

        for n in nums:
            if n != max_val:
                if max_val >= 2 * n:
                    continue
                else:
                    return -1
        return max_index