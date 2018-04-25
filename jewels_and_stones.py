'''
Problem Number: 771
Difficulty level: Easy
Link: https://leetcode.com/problems/jewels-and-stones
'''
'''
Input: J = "aA", S = "aAAbbbb"
Output: 3

Input: J = "z", S = "ZZ"
Output: 0
'''


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel_list = list(J)
        stone_list = list(S)
        jewel_count = 0

        for each_stone in stone_list:
            if each_stone in jewel_list:
                jewel_count += 1

        return jewel_count


# J = "aA"
J = "z"
# S = "aAAbbbb"
S = "ZZ"
obj1 = Solution()
output = obj1.numJewelsInStones(J, S)
print(output)
