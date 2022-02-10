# Lintcode 2949//Easy
# Given a list list_1 with one and only one number appearing an odd number of times and all other numbers appearing an even number of times, find this number and print it out.

# Example
# The evaluator will execute your code using python main.py <{input_path}. You are asked to find the number that appears an odd number of times and print it out, as required by the question.
# Sample example one.
# Input.
# [1, 2, 4, 4, 2]
# Output.
# 1
# Sample II.
# Input.
# [2, 2, 4, 4, 9, 9, 5, 5, 5]
# Output.
# 5

# Challenge
# Can you complete this problem with O(N) time complexity and O(1) additional space complexity.

# Naive solution
# Get List
list_1 = eval(input())
# Please write your code here
val_counts = dict()
for v in list_1:
    if v not in val_counts:
        val_counts[v] = 1
    else:
        val_counts[v] += 1
for v in val_counts:
    if val_counts[v] % 2 == 1:
        print(v)
        break

# Optimal Solution: O(N) time complexity and O(1) additional space complexity
# Use bit-wise XOR. It has the following properties:
# Commutative: A ^ B = B ^ A
# Associative: (A ^ B) ^ C = A ^ (B ^ C)
# Identity element: A ^ 0 = A
# Self-inverse: A ^ A = 0
# XOR of all elements gives odd occurring elements by applying commutative & associative properties to cancel out all elements appearing even times.

list_1 = eval(input())
# Please write your code here
res = 0
for v in list_1:
    res = res ^ v
print(res)
