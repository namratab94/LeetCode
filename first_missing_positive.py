'''
Problem Number: 41
Difficulty level: Hard
Link: https://leetcode.com/problems/first-missing-positive/description/
Author: namratabilurkar
'''

'''
Input: [1,2,0]
Output: 3

Input: [3,4,-1,1]
Output: 2

Input: [7,8,9,11,12]
Output: 1
'''


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest_pos_int = float("inf")
        upper_bound_int = -1

        for n in nums:
            if 0 < n < smallest_pos_int:
                smallest_pos_int = n

        for n in nums:
            if upper_bound_int < n >= smallest_pos_int:
                upper_bound_int = n

        # print("lower bound: " + str(smallest_pos_int))
        # print("upper bound: " + str(upper_bound_int))

        if smallest_pos_int > 1:
            print(1)
            return 1

        # Check if using the sets without storing them in variables still occupies space
        actual_set = set(range(smallest_pos_int,upper_bound_int+1,1))
        given_set = set(nums)
        diff_list = list(actual_set.difference(given_set))

        if len(diff_list) == 0:
            return upper_bound_int + 1
        else:
            return min(diff_list)



class SolutionTest():

    def test1(self, num):
        assert(num == 3)
        # return None

    def test2(self, num):
        assert(num == 2)
        # return None

    def test3(self, num):
        assert (num == 1)
        # return None


op = Solution()
output = SolutionTest()
output.test1(op.firstMissingPositive(nums = [1,2,0])) # 3
# output.test1(op.firstMissingPositive(nums = [1])) # 2
# output.test1(op.firstMissingPositive(nums = [1, 1000])) # 2
output.test2(op.firstMissingPositive(nums = [3,4,-1,1])) # 2
output.test3(op.firstMissingPositive(nums = [7,8,9,11,12])) # 1
# output.test3(op.firstMissingPositive(nums = [-1,4,2,1,9,10])) # 3