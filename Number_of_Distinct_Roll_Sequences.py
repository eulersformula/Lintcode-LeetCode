# Leetcode 2318//Hard

# You are given an integer n. You roll a fair 6-sided dice n times. Determine the total number of distinct sequences of rolls possible such that the following conditions are satisfied:

# The greatest common divisor of any adjacent values in the sequence is equal to 1.
# There is at least a gap of 2 rolls between equal valued rolls. More formally, if the value of the ith roll is equal to the value of the jth roll, then abs(i - j) > 2.
# Return the total number of distinct sequences possible. Since the answer may be very large, return it modulo 109 + 7.

# Two sequences are considered distinct if at least one element is different.

# Example 1:

# Input: n = 4
# Output: 184
# Explanation: Some of the possible sequences are (1, 2, 3, 4), (6, 1, 2, 3), (1, 2, 3, 1), etc.
# Some invalid sequences are (1, 2, 1, 3), (1, 2, 3, 6).
# (1, 2, 1, 3) is invalid since the first and third roll have an equal value and abs(1 - 3) = 2 (i and j are 1-indexed).
# (1, 2, 3, 6) is invalid since the greatest common divisor of 3 and 6 = 3.
# There are a total of 184 distinct sequences possible, so we return 184.
# Example 2:

# Input: n = 2
# Output: 22
# Explanation: Some of the possible sequences are (1, 2), (2, 1), (3, 2).
# Some invalid sequences are (3, 6), (2, 4) since the greatest common divisor is not equal to 1.
# There are a total of 22 distinct sequences possible, so we return 22.

# Constraints:

# 1 <= n <= 10^4

# 一开始的错误解法: 同时记录t时刻和(t-1)时刻以i结尾的符合条件sequence的个数。在(t+1)时刻，用符合条件的t时刻的sequence数目减去(t-1)时刻与(t+1)时刻结尾字符相同的sequence数目。
# 错误原因：t时刻的sequence并未包含(t-1)时刻的某些sequence。比如(t-1)时刻(..., 2, 1)并不会在(t-2)时刻的以2结尾的sequence中（即不存在(..., 2, 1, 2)）
class Solution:
    def distinctSequences(self, n: int) -> int:
        # x[i] = 1; x[i-1] = 2,3,4,5,6; x[i-2] != 1
        # x[i] = 2; x[i-1] = 1,3,5; x[i-2]!=2
        # x[i] = 3; x[i-1] = 1,2,4,5; x[i-2]!=3
        # x[i] = 4; x[i-1] = 1,3,5; x[i-2]!=4
        # x[i] = 5; x[i-1] = 1,2,3,4,6; x[i-2] != 5
        # x[i] = 6; x[i-1] = 1,5; x[i-2] != 5
        # n = 1: [1, 1, 1, 1, 1, 1]
        # n = 2: [5, 3, 4, 3, 5, 2]
        
        res = [[0]*6, [1]*6]
        if n == 1:
            return sum(res[1])
        for _ in range(n-1):
            tmp = [0] * 6
            tmp[0] = res[1][1] + res[1][2] + res[1][3] + res[1][4] + res[1][5]
            tmp[0] -= 5 * res[0][0]
            tmp[1] = res[1][0] + res[1][2] + res[1][4]
            tmp[1] -= 3 * res[0][1]
            tmp[2] = res[1][0] + res[1][1] + res[1][3] + res[1][4]
            tmp[2] -= 4 * res[0][2]
            tmp[3] = res[1][0] + res[1][2] + res[1][4]
            tmp[3] -= 3 * res[0][3]
            tmp[4] = res[1][0] + res[1][1] + res[1][2] + res[1][3] + res[1][5]
            tmp[4] -= 5 * res[0][4]
            tmp[5] = res[1][0] + res[1][4]
            tmp[5] -= 2 * res[0][5]
            res[0] = res[1].copy()
            res[1] = tmp
            print(res)
        return sum(res[1])

class Solution:
    def distinctSequences(self, n: int) -> int:
        # x[i] = 1; x[i-1] = 2,3,4,5,6; x[i-2] != 1
        # x[i] = 2; x[i-1] = 1,3,5; x[i-2]!=2
        # x[i] = 3; x[i-1] = 1,2,4,5; x[i-2]!=3
        # x[i] = 4; x[i-1] = 1,3,5; x[i-2]!=4
        # x[i] = 5; x[i-1] = 1,2,3,4,6; x[i-2] != 5
        # x[i] = 6; x[i-1] = 1,5; x[i-2] != 5
        # n = 1: [1, 1, 1, 1, 1, 1]
        # n = 2: [5, 3, 4, 3, 5, 2]
        if n == 1:
            return 6
        valid_prev_num = {1:[2,3,4,5,6]}
        valid_prev_num.update({2:[1,3,5]})
        valid_prev_num.update({3:[1,2,4,5]})
        valid_prev_num.update({4:[1,3,5]})
        valid_prev_num.update({5:[1,2,3,4,6]})
        valid_prev_num.update({6:[1,5]})
        res = [[0 for _ in range(6)] for _ in range(6)] # stores the last two numbers
        for i in valid_prev_num:
            for j in valid_prev_num[i]:
                res[i-1][j-1] = 1
        # print(res)
        # print(sum(sum(x) for x in res))
        for _ in range(n-2):
            tmp = [[0 for _ in range(6)] for _ in range(6)]
            for i in valid_prev_num:
                for j in valid_prev_num[i]:
                    tmp[i-1][j-1] += sum(res[j-1][k-1] for k in valid_prev_num[j] if i != k)
            res = tmp
            # print(res)
            # print(sum(sum(x) for x in res))
        return sum(sum(x) for x in res) % int(1e9+7)
