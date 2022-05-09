# Lintcode 1886//Easy

from typing import (
    List,
)

# 我写的Solution: T = O(n); S = O(1)
class Solution:
    """
    @param nums: a list of integer
    @param target: an integer
    @return: nothing
    """
    def move_target(self, nums: List[int], target: int):
        # write your code here
        if len(nums) == 0:
            return nums
        r = len(nums) - 1
        while r > 0 and nums[r] != target:
            r -= 1
        l = r - 1 # l >= 0
        while r > 0: # if r == 0, no need to do swaps
            # 一开始在此处写l = r - 1, O(T)变成O(n^2)
            while l >= 0 and nums[l] == target:
                l -= 1
            if l < 0:
                break
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
            l -= 1
        return nums

# 标准答案: T = O(n); S = O(1)
from typing import (
    List,
)

class Solution:
    """
    @param nums: a list of integer
    @param target: an integer
    @return: nothing
    """
    def move_target(self, nums: List[int], target: int):
        l, r = len(nums) - 1, len(nums) - 1
        while l >= 0:
            if nums[l] == target:
                l -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l -= 1
                r -= 1
        return nums

# 另一种解法：T = O(n); S = O(n)
class Solution:
    """
    @param nums: a list of integer
    @param target: an integer
    @return: nothing
    """
    def move_target(self, nums: List[int], target: int):
        # write your code here
        if len(nums) == 0:
            return nums
        l1 = [x for x in nums if x != target]
        res = [target] * (len(nums) - len(l1)) + l1
        for (i, v) in enumerate(res):
            nums[i] = v
