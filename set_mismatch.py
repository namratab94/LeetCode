'''
Problem Number: 645
Difficulty level: Easy
Link: https://leetcode.com/problems/set-mismatch/description/
Author: namratabilurkar
'''

'''
Input: nums = [1,2,2,4]
Output: [2,3]
'''


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_of_nums = sum(nums)

        repeated_num = sum_of_nums - sum(set(nums))

        list_len = len(nums)

        expected_nums_total = 0

        for i in range(1, list_len+1):
            expected_nums_total += i

        # Gap between the expected total of 1 to n numbers and the actual sum of nums.
        gap = expected_nums_total - sum_of_nums

        disappeared_num = repeated_num + gap

        return [repeated_num, disappeared_num]



output = Solution()
print(output.findErrorNums(nums=[1,2,2,4])) # [2,3]
print(output.findErrorNums(nums=[2,2,3,4,5,6])) # [2,1]
print(output.findErrorNums(nums=[1,2,3,4,5,4])) # [4,6]