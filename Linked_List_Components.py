# Lintcode 1371//Medium//Google

# Description
# We are given head, the head node of a linked list containing unique integer values.

# We are also given the list G, a subset of the values in the linked list.

# Return the number of connected components in G, where two values are connected if they appear consecutively(the longest) in the linked list.

# If N is the length of the linked list given by head, 1 \leq N \leq 100001≤N≤10000.
# The value of each node in the linked list will be in the range [0, N - 1].
# 1 \leq G.length \leq 100001≤G.length≤10000.
# G is a subset of all values in the linked list.
# Example
# Example 1:

# Input: head = 0->1->2->3, G = [0, 1, 3]
# Output: 2
# Explanation: 
# 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
# Example 2:

# Input: head = 0->1->2->3->4, G = [0, 3, 1, 4]
# Output: 2
# Explanation: 
# 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.

from typing import (
    List,
)
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

class Solution:
    """
    @param head: the head
    @param g: an array
    @return: the number of connected components in G
    """
    def num_components(self, head: ListNode, g: List[int]) -> int:
        # Write your code here
        # Questions to ask:
        # 1. Is it guaranteed that the values in g will appear in the linked list?
        # 2. Is it possible for the same value to appear more than once in g?
        if len(g) == 0:
            return 0
        if head is None:
            return len(g)
        g = set(g)
        in_component = False
        n_components = 0
        while head is not None:
            cur_v = head.val
            if cur_v not in g:
                if in_component:
                    n_components += 1
                    in_component = False
            else:
                if not in_component:
                    in_component = True
                g.remove(cur_v)
            head = head.next
        if in_component:
            n_components += 1
        return n_components
