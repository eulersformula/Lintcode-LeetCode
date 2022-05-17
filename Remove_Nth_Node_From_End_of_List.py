# Leetcode 19//Medium
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 
# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Questions to ask:
        # 1. What is the range of n? Is it possible to be 0? Is it possible n greater than the number of nodes in the linked list?
        # 2. Is it possible for head to be None?
        if head is None:
            return None
        orig_head, orig_head_2 = head, head
        cnt = 0
        head_1, prev, head_2 = head, None, None
        while head_1 is not None:
            if cnt == n-1:
                head_2 = orig_head_2
            elif cnt > n-1:
                prev = head_2
                head_2 = head_2.next
            cnt += 1
            head_1 = head_1.next
        if cnt == 1 and n == 1:
            return None
        if prev is None:
            return head_2.next
        if n == 1:
            prev.next = None
        else:
            prev.next = head_2.next
        return orig_head 
