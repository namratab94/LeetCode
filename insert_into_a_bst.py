'''
Problem Number: 701
Difficulty level: Medium
Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
Author: namratabilurkar
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root.val < val:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        elif root.val > val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        return root