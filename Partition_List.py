# Lintcode 96//Easy

# Description
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Example
# Example 1:

# Input:

# list = null
# x = 0
# Output:

# null
# Explanation:

# The empty list Satisfy the conditions by itself.

# Example 2:

# Input:

# list = 1->4->3->2->5->2->null
# x = 3
# Output:

# 1->2->2->4->3->5->null
# Explanation:

# keep the original relative order of the nodes in each of the two partitions.

from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# T: O(n); S: O(n)

class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head: ListNode, x: int) -> ListNode:
        # write your code here
        if head is None:
            return head
        lt_head, lt_st = None, None
        geq_head, geq_st = None, None
        while head is not None:
            if head.val < x:
                if lt_head is None:
                    lt_head = head
                    lt_st = head
                else:
                    lt_head.next = head
                    lt_head = head
            else:
                if geq_head is None:
                    geq_head = head
                    geq_st = head
                else:
                    geq_head.next = head
                    geq_head = head
            head = head.next
        if lt_st is None:
            return geq_st
        if geq_st is None:
            return lt_st
        geq_head.next = None
        lt_head.next = geq_st
        return lt_st # 该行一开始写错写成lt_head了
      
