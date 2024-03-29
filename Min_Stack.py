# Lintcode 12//Medium//Google//Uber//...

# Description

# Implement a stack with min() function, which will return the smallest number in the stack.

# It should support push, pop and min operation all in O(1) cost.

# Example
# push(1)
# pop()   // return 1
# push(2)
# push(3)
# min()   // return 2
# push(1)
# min()   // return 1

class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack1 = []
        self.stack2 = []

    def push(self, number):
        # write yout code here
        self.stack1.append(number)
        if self.stack2 == [] or number <= self.stack2[-1]:
            self.stack2.append(number)
        
    def pop(self):
        # pop and return the top item in stack
        val = self.stack1.pop()
        if val == self.stack2[-1]:
            self.stack2.pop()

# Single stack solution
class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = list()

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        if len(self.stack) == 0 or self.stack[-1][1] > number:
            cur_min_val = number
        else:
            cur_min_val = self.stack[-1][1]
        self.stack.append((number, cur_min_val))

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        return self.stack.pop()[0]

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self.stack[-1][1]
        return val
        
    def min(self):
        # return the minimum number in stack
        return self.stack2[-1]

# 单调栈版本
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_vals = [] # 从开始到当前元素的最小值
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0 or val <= self.min_vals[-1]:
            self.min_vals.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_vals[-1]:
            self.min_vals.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]

