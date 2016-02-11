#Reverse a linked list.

#Example
#For linked list 1->2->3, the reversed linked list is 3->2->1

#Challenge
#Reverse it in-place and in one-pass

"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        prev = None #notice the use of anchor node
        cur = head
        while cur != None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev
