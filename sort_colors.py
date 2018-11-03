'''
Problem Number: 75
Difficulty level: Medium
Link: https://leetcode.com/problems/sort-colors/description/
Author: namratabilurkar
'''


class Solution(object):
    def sortColors(self, nums):
        i = 0
        j = -1
        k = 0
        for _ in range(len(nums)):
            if nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                k += 1
            elif nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
            else:
                k += 1


obj = Solution()
alist = [2,0,2,1,1,0]
obj.sortColors(alist)
print(alist)