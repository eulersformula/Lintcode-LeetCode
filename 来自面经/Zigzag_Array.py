# Mobikwik//Easy
# Given an array of distanct elements, reaarange the elements of an array in zig-zag fashion in O(n) time. 
# The converted array should be in form a < b > c < d > e < f.

from typing import List

# T: O(n); S: O(1)

def zigzag(nums: List[int]) -> List[int]:
    # Can be proved by induction
    if len(nums) <= 1:
        return nums
    idx = 1
    while idx < len(nums):
        if (idx % 2 == 0) and (nums[idx] > nums[idx-1]) or \
            (idx % 2 != 0) and (nums[idx] < nums[idx-1]) :
            nums[idx], nums[idx-1] = nums[idx-1], nums[idx]
        idx += 1
    return nums
