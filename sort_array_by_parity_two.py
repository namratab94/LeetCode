'''
Problem Number: 922
Difficulty level: Easy
Link: https://leetcode.com/problems/sort-array-by-parity-ii/
Author: namratabilurkar
'''

'''
Input: [4,2,5,7]

Output: [4,5,2,7]

Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
'''

class Solution(object):
    def isEven(self, num):

        return num % 2

    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # i is used to track the even indices
        # j is used to track the odd indices

        n = len(A)

        j = 1
        for i in range(0, n, 2):
            if self.isEven(A[i]):
                while self.isEven(A[j]):
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
