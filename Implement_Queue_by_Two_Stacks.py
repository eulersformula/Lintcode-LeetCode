#As the title described, you should only use two stacks to implement a queue's actions.
#The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.
#Both pop and top methods should return the value of first element.

#Example:
#push(1)
#pop()     // return 1
#push(2)
#push(3)
#top()     // return 2
#pop()     // return 2

#Chanllenge: implement it by two stacks, do not use any other data structure and push, pop and top should be O(1) by AVERAGE.

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def change(self): #remember to put repetitive code in a new function
        if self.stack1 == []:
            while self.stack2 != []:
                p = self.stack2.pop()
                self.stack1.append(p)
                
    def push(self, element):
        self.stack2.append(element)

    def top(self):
        # return the top element
        self.change()
        if self.stack1 == []:
            return None
        return self.stack1[-1]
                
    def pop(self):
        # write your code here
        # pop and return the top element
        self.change()
        if self.stack1 == []:
            return None
        return self.stack1.pop()
