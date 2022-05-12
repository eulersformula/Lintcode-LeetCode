# Lintcode 1302//Easy//NetEase

# Description
# The monthly salary of the employees of Xiaoming ’s company is x[i] yuan.
# Now the boss of Xiaomin asks Xiaomin several times, and every time he asks the boss, he will give an integer k. Xiaomin should quickly answer the number of employees whose salary is equal to k.

# 1 \leq wage.size() \leq 800001≤wage.size()≤80000
# 1 \leq ask.size() \leq 1000001≤ask.size()≤100000
# 1 \leq wage[i] \leq 500,000,0001≤wage[i]≤500,000,000
# Example
# Example 1:

# Input: wage = [6,2,1,2,6,2,5],ask = [6,5,8,2]
# Output: [2,1,0,3]

from typing import (
    List,
)

class Solution:
    """
    @param wage: Salaries of all employees
    @param ask: Number of inquiries
    @return: Every time an answer is asked
    """
    def people_counting(self, wage: List[int], ask: List[int]) -> List[int]:
        # write your code here
        wage_count = dict()
        for w in wage:
            if w not in wage_count:
                wage_count[w] = 0
            wage_count[w] += 1
        res = []
        for a in ask:
            if a in wage_count:
                res.append(wage_count[a])
            else:
                res.append(0)
        return res
