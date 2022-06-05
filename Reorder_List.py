# Leetcode 143//Medium
# Lintcode 99//Medium
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Change value: T: O(n); S: O(n)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        vals = []
        orig_head = head
        while head is not None:
            vals.append(head.val)
            head = head.next
        # print(vals)
        st, ed = 0, len(vals) - 1
        head, cnt = orig_head, 0
        while head is not None:
            if cnt % 2 == 0:
                head.val = vals[st]
                st += 1
            else:
                head.val = vals[ed]
                ed -= 1
            cnt += 1
            head = head.next

# In Place: T: O(n^2); S: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        if head is None:
            return None
        prev = None
        while head is not None:
            tmp, head.next = head.next, prev
            prev, head = head, tmp
        return prev
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        while head is not None:
            head.next = self.reverseList(head.next)
            head = head.next

# In place 
