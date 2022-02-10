# Lintcode 2938//Medium

# Description
# Given an unfinished linked list class LinkedList, complete the iterable methods of this class and iterate over the instances of this class to obtain the complete linked list.

# Example
# The evaluator will execute your code via python main.py {input_path}, and you need to complete the class LinkedList.
# Sample example one.
# Input.
# 19->54
# Output.
# [19,54]
# Sample two.
# Input.
# 26->12->30->69->72->47->35->40->44
# Output.
# [26, 12, 30, 69, 72, 47, 35, 40, 44]

# Notice the use of yield for __iter__

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.__length = 0
        self.head = None
        self.tail = None

    def add(self, val):
        newnode = Node(val)
        if self.__length == 0:
            self.head = newnode
            self.tail = self.head
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.__length += 1

    def __iter__(self):
    # Please write your code here
        node = self.head
        while node is not None:
            yield(node.val)
            node = node.next
