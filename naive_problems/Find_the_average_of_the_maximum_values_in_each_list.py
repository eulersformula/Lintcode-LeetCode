# Lintcode 2959//Easy
# Description
# Given a list list_1 with multiple nested lists, calculate the maximum value of each nested list and output the average of all the maximum values.

# Example
# The evaluator executes your code with python main.py <{input_path}. You are asked to find the maximum value of the nested list, then average those values, keep the result to two decimal places, and print it out on the console.
# Example 1.
# Input.

# [[54, 28, 88, 99, 77],[99, 6, 37, 68, 83],[90, 52, 36, 4, 53],[85, 66, 11, 11, 61],[20, 52, 9, 81, 61],[23, 67, 37, 39, 18],[21, 36, 66, 80, 30],[74, 80, 5, 7, 96],[30, 35, 71, 73, 4],[40, 67, 67, 11, 71]]
# Output.

# 84.10
# Explanation.
# The maximum value of nested list one is 3, and the maximum value of nested list two is 4. Find the average value of 3.50
# Example II.
# Input.

# [[5,3],[2,3,4], [5,5,6]]
# Output.

# 7.50

list_1 = eval(input())
# Please your code here
s = 0.
for ls in list_1:
    s += max(ls)
print('%.2f'%(s/len(list_1)))
