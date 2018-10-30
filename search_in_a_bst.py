'''
Problem Number: 700
Difficulty level: Easy
Link: https://leetcode.com/problems/search-in-a-binary-search-tree/
Author: namratabilurkar
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        outputTree = []
        if root == None:
            return outputTree

        while root != None:
            if val == root.val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right