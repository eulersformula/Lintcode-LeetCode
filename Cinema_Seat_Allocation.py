# Leetcode 1386//Medium

# A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

# Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.

# Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.

# Example 1:
# Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
# Output: 4
# Explanation: The figure above shows the optimal allocation for four groups, where seats mark with blue are already reserved and contiguous seats mark with orange are for one group.
# Example 2:
# Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
# Output: 2
# Example 3:
# Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
# Output: 4
# Constraints:

# 1 <= n <= 10^9
# 1 <= reservedSeats.length <= min(10*n, 10^4)
# reservedSeats[i].length == 2
# 1 <= reservedSeats[i][0] <= n
# 1 <= reservedSeats[i][1] <= 10
# All reservedSeats[i] are distinct.

# 总结：能用hashmap和set的就不要用list of list以节约空间
# T: O(m); S: O(n); m is length of reservedSeats

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # reserved_seats_by_row = [[0 for _ in range(10)] for _ in range(n)] # 一开始该行写错。使用list会导致memory溢出。
        reserved_seats_by_row = dict()
        for (i, j) in reservedSeats:
            i, j = i - 1, j - 1
            if i not in reserved_seats_by_row:
                reserved_seats_by_row[i] = set()
            reserved_seats_by_row[i].add(j)
        config_counts = dict()
        config_counts[(0,)*10] = n - len(reserved_seats_by_row) # 一开始漏掉了该情况
        for (_, s) in reserved_seats_by_row.items():
            config = [0] * 10
            for idx in s:
                config[idx] = 1
            config = tuple(config)
            config_counts[config] = 1 if config not in config_counts else config_counts[config] + 1
        res = 0
        for (config, cnt) in config_counts.items():
            if sum(config[1:5]) == 0 and sum(config[5:9]) == 0:
                res += cnt * 2
                continue
            if sum(config[1:5]) == 0 or sum(config[5:9]) == 0 or sum(config[3:7]) == 0:
                res += cnt
                continue
        return res
