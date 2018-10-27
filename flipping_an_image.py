'''
Problem Number: 832
Difficulty level: Easy
Link: https://leetcode.com/problems/flipping-an-image/
Author: namratabilurkar
'''

'''
Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
'''


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        final_list = list()
        for sub_list in A:
            temp = list()
            sbl_len = len(sub_list)
            for i in range(sbl_len):
                if sub_list[i] == 0:
                    val = 1
                elif sub_list[i] == 1:
                    val = 0
                temp.append(val)
            t2 = []
            for i in range(len(temp)-1,-1,-1):
                t2.append(temp[i])
            final_list.append(t2)
        return final_list


obj = Solution()
# op = obj.flipAndInvertImage(A=[[1,1,0],[1,0,1],[0,0,0]])
op = obj.flipAndInvertImage(A=[[1,1,0],[1,0,1],[0,0,0]])
# op = obj.flipAndInvertImage(A=[[1,0,1]])
print(op==[[1,0,0],[0,1,0],[1,1,1]])
