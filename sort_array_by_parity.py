'''
Problem Number: 905
Difficulty level: Easy
Link: https://leetcode.com/problems/sort-array-by-parity/
Author: namratabilurkar
'''

'''
Input: [3,1,2,4]

Output: [2,4,3,1]

The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        '''
        Maintain an even and an odd pointer and use them to swap the even and odd values in place. 
        '''
        even = 0
        odd = len(A) - 1

        while even < odd:
            if A[even] % 2 > A[odd] % 2:
                A[even], A[odd] = A[odd], A[even]

            if A[even] % 2 == 0:
                even += 1
            if A[odd] % 2 == 1:
                odd -= 1

        return A