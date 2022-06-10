# Lintcode 859//Hard//LinkedIn

# Description
# Design a max stack that supports push, pop, top, peekMax and popMax.

# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
# -1e7 <= x <= 1e7
# Number of operations won't exceed 10000.
# The last four operations won't be called when stack is empty.
# Example
# Input:
# push(5)
# push(1)
# push(5)
# top()
# popMax()
# top()
# peekMax()
# pop()
# top()
# Output:
# 5
# 5
# 1
# 5
# 1
# 5

class MaxStack:
    def __init__(self):
        # do intialization if necessary
        self.stack = list()
        self.length = 0
    
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        if self.length == 0 or self.stack[-1][1] <= x:
            cur_max, max_idx = x, self.length
        else:
            cur_max, max_idx = self.stack[-1][1], self.stack[-1][2]
        self.stack.append([x, cur_max, max_idx])
        self.length += 1

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        self.length -= 1
        return self.stack.pop()[0] # 一开始此处忘了return

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.stack[-1][0]

    """
    @return: An integer
    """
    def peekMax(self):
        # write your code here
        return self.stack[-1][1]

    """
    @return: An integer
    """
    def popMax(self):
        # write your code here
        max_idx = self.stack[-1][2]
        prev_element = self.stack[max_idx-1] if max_idx > 0 else None # if None, first element is popped
        for idx in range(max_idx+1, self.length):
            if prev_element is None:
                self.stack[idx][1] = self.stack[idx][0]
                self.stack[idx][2] = 0
            elif self.stack[idx][0] >= prev_element[1]:
                self.stack[idx][1] = self.stack[idx][0]
                self.stack[idx][2] = idx - 1
            else:
                self.stack[idx][1] = prev_element[1]
                self.stack[idx][2] = prev_element[2]
            prev_element = self.stack[idx]
        self.length -= 1
        return self.stack.pop(max_idx)[0]

# 单调栈版本
class MaxStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.maxStack = []
    
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        if len(self.maxStack) == 0 or x >= self.maxStack[-1]:
            self.maxStack.append(x)
        self.stack.append(x)
        # print(self.stack, self.maxStack)

    """
    @return: An integer
    """
    def pop(self): # 要求return top element
        # write your code here
        val = self.stack.pop()
        if val == self.maxStack[-1]:
            self.maxStack.pop()
        return val
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.stack[-1]

    """
    @return: An integer
    """
    def peekMax(self):
        # write your code here
        return self.maxStack[-1]

    """
    @return: An integer
    """
    def popMax(self): # 题目没说清是否要返回pop值。但例子中有说明
        # write your code here
        # 此处每次pop后要用pop元素之后的值重新更新一边stack和max stack。
        # 比如[1, 5, 1, 5]在popMax两次以后，最大值栈已清空
        tmpStack = []
        v = self.stack.pop()
        while v != self.maxStack[-1]:
            tmpStack.append(v)
            v = self.stack.pop()
        v = self.maxStack.pop()
        while len(tmpStack) > 0:
            self.push(tmpStack.pop())
        return v
