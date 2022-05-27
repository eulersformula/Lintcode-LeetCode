# Lintcode 1861//Hard//Google

# Description
# There is a mouse jumping from the top of a staircase with height n. This mouse can jump 1, 3 or 4 steps in an even number of jumps and 1, 2, or 4 steps in an odd number of times. Some steps have glue,if the mouse jump those steps,it will be directly stuck and cannot continue to jump.You need to solve how many ways the mouse can reach the ground ( level 0 ) from the top of this staircase.It also can be reached if it exceeds the ground. For example, jumping from 1 to -1 is another plan for jumping from 1 to 0.The state of the stairs with or without glue is input from high to low, that is, arr[0] is the top of the stairs.
# arr[i] == 0 represents that there is no glue on the i-th position, arr[i] == 1 represents that there is glue on the i-th position.

# 2<=n<=50000
# arr[i]=1 means there is glue on the step, 0 means there is no glue
# The input guarantees the highest steps and the lowest is 0
# The answer needs to be modulo by 1e9 + 7

# Example
# Example1:

# Input:
# [0,0,0]
# Output:
# 5
# Explanation:
# There are 3 steps.
# The step 2  is the starting point without glue.
# Step 1, no glue.
# Step 0, no glue.
# The mouse jump plans is:
# 2--odd(1)-->1--even(1)-->0
# 2--odd(1)-->1--even(3)-->-2
# 2--odd(1)-->1--even(4)-->-3
# 2--odd(2)-->0
# 2--odd(4)-->-2
# Example2:

# Input:
# [0,0,1,0]
# Output:
# 3
# Explanation:
# There are 4 steps.
# The step 3  is the starting point without glue.
# Step 2, no glue.
# Step 1, have glue.
# Step 0, no glue.

from typing import (
    List,
)

# TRIAL 1: BFS. CORRECT BUT TIME LIMIT EXCEEDED

class Solution:
    """
    @param arr: the steps whether have glue
    @return: the sum of the answers
    """
    def rat_jump(self, arr: List[int]) -> int:
        # Write your code here.
        # Questions to ask:
        # 1. What is the range of the length of the array?
        # 2. Clarification: last element of arr is for level 0?
        # 3. Is it OK for level 0 to have glue if rat jumps to level 0?
        if len(arr) == 0:
            return 0
        res = 0
        state_dict = dict()
        n = len(arr) - 1
        state_dict[n] = 1
        n_jumps = 0
        while len(state_dict) > 0:
            # guarantees that the paths are different since no same level after 
            # the same number of jumps throughout.
            cur_state_dict = dict()
            n_jumps += 1
            for level in state_dict:
                if level <= 0:
                    res += state_dict[level]
                    # 本来此行加了state_dict.pop(level)，显示错误
                    # dictionary changed size during iteration
                elif arr[n-level] == 0: #if 1, throw away
                    if n_jumps % 2 == 0:
                        for v in [1, 3, 4]:
                            if (level - v) not in cur_state_dict:
                                cur_state_dict[level-v] = 0
                            cur_state_dict[level-v] += state_dict[level]
                    else:
                        for v in [1, 2, 4]:
                            if (level - v) not in cur_state_dict:
                                cur_state_dict[level-v] = 0
                            cur_state_dict[level-v] += state_dict[level]
            state_dict = cur_state_dict
        return res % int(1e9+7)
