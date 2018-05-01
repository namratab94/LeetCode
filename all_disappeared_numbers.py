'''
Problem Number: 448
Difficulty level: Easy
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
Author: namratabilurkar
'''

'''
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_of_nums = len(nums)

        expected_list = []

        for i in range(1, len_of_nums+1):
            expected_list.append(i)

        disappeared_num_array = list(set(expected_list).difference(set(nums)))

        return disappeared_num_array


output = Solution()
print(output.findDisappearedNumbers(nums=[4,3,2,7,8,2,3,1])) # [5,6]