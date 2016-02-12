#Implement a stack with min() function, which will return the smallest number in the stack.

#It should support push, pop and min operation all in O(1) cost.

#Example
#push(1)
#pop()   // return 1
#push(2)
#push(3)
#min()   // return 2
#push(1)
#min()   // return 1

#Idea is to use two stacks: one to keep the whole sequence, the other to update minimum number

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
        return val
        
    def min(self):
        # return the minimum number in stack
        return self.stack2[-1]
