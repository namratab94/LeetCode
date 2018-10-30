'''
Problem Number: 589
Difficulty level: Easy
Link: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
Author: namratabilurkar
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output = []
        if root is None:
            return output

        stack = [root, ]
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])

        return output
