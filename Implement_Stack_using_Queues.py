# Leetcode 225//Easy
# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
 

# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
 

# Follow-up: Can you implement the stack using only one queue?

class MyNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None

class MyQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def push(self, x: int) -> None:
        if self.size == 0:
            self.head = MyNode(x)
            self.tail = self.head
        else:
            self.tail.next = MyNode(x)
            self.tail = self.tail.next
        self.size += 1
    
    def empty(self) -> bool:
        return (self.size == 0)
    
    def peek(self) -> int:
        return self.head.val
    
    def peeklast(self) -> int:
        return self.tail.val
        
    def pop(self) -> int:
        if self.size == 0:
            return None
        res = self.head.val
        if self.size == 1:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next
        self.size -= 1
        return res
    

class MyStack:

    def __init__(self):
        self.queue_1 = MyQueue()
        self.queue_2 = MyQueue()

    def push(self, x: int) -> None:
        if self.queue_2.empty():
            self.queue_1.push(x)
        else:
            self.queue_2.push(x)

    def pop(self) -> int:
        if self.queue_1.empty() and self.queue_2.empty():
            return None
        if self.queue_1.empty():
            len_queue_2 = self.queue_2.size
            for _ in range(len_queue_2 - 1):
                self.queue_1.push(self.queue_2.pop()) # List只有pop()没有popleft()
            return self.queue_2.pop()
        len_queue_1 = self.queue_1.size
        for _ in range(len_queue_1 - 1):
            self.queue_2.push(self.queue_1.pop())
        return self.queue_1.pop()

    def top(self) -> int:
        if self.queue_1.empty() and self.queue_2.empty():
            return None
        if self.queue_2.empty():
            return self.queue_1.peeklast()
        return self.queue_2.peeklast()

    def empty(self) -> bool:
        return self.queue_1.empty() and self.queue_2.empty()

# Follow-up
class MyStack: # S: O(n)

    def __init__(self):
        self.queue = MyQueue()

    def reverse(self): # T: O(n)
        if self.queue.size > 1:
            prev_node, node = None, self.queue.head
            while node is not None:
                #执行顺序，先把现在node.next赋给tmp，再把prev赋给node.next
                tmp, node.next = node.next, prev_node
                #执行顺序，先把现在node赋给prev，再把tmp赋给node
                prev_node, node = node, tmp 
            self.queue.head = prev_node
                
    def push(self, x: int) -> None: # T: O(1)
        self.queue.push(x)

    def pop(self) -> int: # T: O(n)
        self.reverse()
        res = self.queue.pop()
        self.reverse()
        return res

    def top(self) -> int: # T: O(n)
        self.reverse()
        res = self.queue.peek()
        self.reverse()
        return res

    def empty(self) -> bool: # T: O(1)
        return self.queue.empty()
