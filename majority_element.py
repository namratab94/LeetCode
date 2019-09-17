'''
Problem Number: 169
Difficulty level: Easy
Link: https://leetcode.com/problems/majority-element/
Author: namratabilurkar
'''

'''
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = dict()
        
        for num in nums:
            if num not in num_count:
                num_count[num] = 0
            num_count[num] += 1
            
        occurrences = num_count.items()
        
        max_occurrence = 0
        max_freq_num = -1
        for each in occurrences:
            occurrence = each[1]
            num = each[0]
            if occurrence > max_occurrence:
                max_occurrence = occurrence
                max_freq_num = num
        
        return max_freq_num



output = Solution()
print(output.majorityElement(nums=[1,2,2,4])) # 2
print(output.majorityElement(nums=[2,2,3,4,5,7,5,5,6,5,6])) # 5