# Leetcode 985//Medium

# You are given an integer array nums and an array queries where queries[i] = [vali, indexi].

# For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.

# Return an integer array answer where answer[i] is the answer to the ith query.

# Example 1:

# Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]
# Explanation: At the beginning, the array is [1,2,3,4].
# After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
# After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
# After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
# After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
# Example 2:

# Input: nums = [1], queries = [[4,0]]
# Output: [0]
 
# Constraints:

# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# 1 <= queries.length <= 10^4
# -10^4 <= vali <= 10^4
# 0 <= index_i < nums.length

# T: O(n + m); S: O(1) if not considering the space to store the answer

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        even_sum = 0
        for v in nums:
            if v % 2 == 0:
                even_sum += v
        for val, index in queries:
            if nums[index] % 2 == 0: # previously including this element in the sum
                if val % 2 == 0: # continue including
                    even_sum += val
                else: # excluding
                    even_sum -= nums[index]
            else: # previously excluding this element in the sum
                if val % 2 == 1: # otherwise continue excluding
                    even_sum += nums[index] + val
            ans.append(even_sum)
            nums[index] += val
        return ans

       
# 看到有答案说，有负数时，判断奇偶要注意。若采用%2的判断方式，则奇数的条件不能简单写为x % 2 == 1，因为负奇数模2为-1。但是在Python 3下无论正负奇数%2都是为-1
