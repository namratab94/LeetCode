'''
Problem Number: 206
Difficulty level: Easy
Link: https://leetcode.com/problems/reverse-linked-list/
Author: namratabilurkar
'''

'''
prev -> curr -> after
after -> curr -> prev

1. Have a temp node
2. Store the data of after in temp node
3. Store prev.next in temp.next
4. Store prev.data in after.data
5. Set prev.next to null
6. Set temp node to prev node


------- No altering the data of any nodes -------

1. Have a temp node
2. Set temp = prev
3. Set after.next = curr
4. Set prev = after
5. Set after = temp 
6. Set curr.next = after

temp
after <- curr <- prev


------- If curr is head -------

curr(head) -> after

None <- curr <- after

1. curr.next = None
2. after.next = curr

curr <- after

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev

        return head
