# Lintcode 1066//Medium

# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:

# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# Example 3:

# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

# Constraints:

# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 1 <= x <= 10^9

# Trial 1: DP. TLE
from collections import deque
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # same as make the sum equal to x
        # 需要问值的范围、类型、输入、输出（后面给出了nums和x都是正整数）
        len_nums = len(nums)
        if len_nums == 0:
            return -1
        tmp = set([(0, len_nums-1, x)])
        res = None
        step = 0
        while len(tmp) > 0:
            cur = set()
            for t in tmp:
                # print(t)
                left, right, s = t
                if s == 0:
                    return step
                if s < 0:
                    continue
                if left == right:
                    if s - nums[left] == 0:
                        return step + 1
                else:
                    cur.add((left+1, right, s-nums[left]))
                    cur.add((left, right-1, s-nums[right]))
            tmp = cur # 总是忘
            step += 1
        return -1

# Trial 2: T: O(n); S: O(n)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # same as make the sum equal to x
        # 需要问值的范围、类型、输入、输出（后面给出了nums和x都是正整数）
        len_nums = len(nums)
        if len_nums == 0:
            return -1
        cur_sum_left, cur_sum_right = 0, sum(nums)
        sum_left, sum_right = [0], []
        for n in nums: # 一开始用x作为变量，导致argument里的x值被覆盖
            cur_sum_left += n
            sum_left.append(cur_sum_left)
            sum_right.append(cur_sum_right)
            cur_sum_right -= n
        sum_right.append(0)
        sum_right.reverse()
        sum_right_dict = {}
        for (idx, v) in enumerate(sum_right):
            sum_right_dict[v] = idx
        res = len_nums + 1
        # print(sum_left, sum_right_dict)
        for (idx, s) in enumerate(sum_left): # 总是忘enumerate
            target = x - s
            if target in sum_right_dict and \
                idx + sum_right_dict[target] <= len_nums:
                res = min(res, idx + sum_right_dict[target])
        if res == len_nums + 1:
            return -1
        return res
