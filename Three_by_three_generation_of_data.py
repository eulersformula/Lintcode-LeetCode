# Lintcode 2169//Medium
# Description
# Please write Python code that takes a string of data as template data and uses a generator 3 by 3 to generate a specified number of entries based on the template data.

# Please write the code to create the generator in solution.py and we will run your code in main.py by importing it to check if your code implements the above functionality.

# If the number of template data is not a multiple of 3,then discard the last insufficient data and start circle again from the first number
# If the template data is less than 3 numbers,then repeat the template data as one piece of dataa
# Example
# Example 1

# When the input data is:
# [1,0,5,5,3,10,9,10,3,5,5,6,7,4,10,8,7,7,7]
# 7 
# the output data is：
# [1, 0, 5]
# [5, 3, 10]
# [9, 10, 3]
# [5, 5, 6]
# [7, 4, 10]
# [8, 7, 7]
# [1, 0, 5]

# Example 2
# When the input data is:
# [8,2,5,10,3,3,0,7,2,1,5,6,6,5,1,6,9]
# 10
# the output data is：
# [8, 2, 5]
# [10, 3, 3]
# [0, 7, 2]
# [1, 5, 6]
# [6, 5, 1]
# [8, 2, 5]
# [10, 3, 3]
# [0, 7, 2]
# [1, 5, 6]
# [6, 5, 1]

class DataLoader:
    def __init__(self, data):
        # write your code here
        if len(data) < 3 or len(data) % 3 == 0:
            self.data = data
            self.length = len(self.data)
        else: # if the length is not a template of 3, first remove the last insufficient data
            length = len(data) // 3 * 3
            self.data = data[:length]
            self.length = length

    def get_data(self):
        # write your code here
        if self.length < 3:
            while True:
                yield(self.data)
        else:
            st = 0
            while True:
                st = st % self.length
                yield(self.data[st:(st+3)])
                st += 3
