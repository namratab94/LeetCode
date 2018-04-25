'''
Problem Number: 136
Difficulty level: Easy
Link: https://leetcode.com/problems/single-number/description/
Author: namratabilurkar
'''

'''
Input: [2,2,1]
Output: 1

Input: [4,1,2,1,2]
Output: 4
'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_dict = {}

        for each_num in nums:
            if each_num not in nums_dict:
                nums_dict[each_num] = 1
            else:
                nums_dict[each_num] += 1


        return min(nums_dict, key=lambda k: nums_dict[k])


# nums = [2,2,1]
nums = [4,1,2,1,2]
output = Solution()
print(output.singleNumber(nums))