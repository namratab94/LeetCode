'''
Problem Number: 485
Difficulty level: Easy
Link: https://leetcode.com/problems/
Author: namratabilurkar
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        # Partially correct solution
        
        max_one_counter = 0
        one_counter = 0
        print ("(i, one_counter, max_one_counter)")
        for i in nums:
            if i == 1:
                one_counter += 1
            elif i == 0 and max_one_counter <= one_counter:
                max_one_counter = one_counter
                one_counter = 0
            print (i, one_counter, max_one_counter)
            if max_one_counter <= one_counter:
                max_one_counter = one_counter
        return max_one_counter

        '''

        one_len_arr = list()
        curr_len = 0

        for i in nums:
            if i == 1:
                curr_len += 1
            else:
                if curr_len != 0:
                    one_len_arr.append(curr_len)
                else:
                    continue
                curr_len = 0

        if curr_len != 0:
            one_len_arr.append(curr_len)

        if len(one_len_arr):
            max_val = max(one_len_arr)
        else:
            max_val = 0
        return max_val