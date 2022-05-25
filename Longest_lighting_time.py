# Lintcode 1916//Easy//Roblox

# Description
# You have 26 lamps in a row, and a list of operations that can switch lamps on or off.
# All of lamps are off from the start, then the lamps will accept these operations one by one.
# Each of operation[i] includes two integers, operation[i][0] and operation[i][1].
# After these lamps accept an operation, the operation[i][0]-th lamp will turn on, and it will turn off at the operation[i][1]-th second.When this lamp turns off, the next operation will be accepted. That is, any time there is only one light is on.
# The first operation will be sent at the 0-th second, and it will be accepted immediately.
# You need to find which lamp has the longest continuously lighting time.

# 1 ≤ n ≤ 10^5
 
# 0≤keyTimes[i][0]≤25 (0≤i<n)
# 0≤keyTimes[i][1]≤10^8 (0≤i<n)
# There will only be one key with the worst time.
# keyTimes is sorted in ascending order of keyTimes[i][1].

# Example
# Example 1

# Input：
# [[0,2],[1,5],[0,9],[2,15]]
# Output：
# 'c'
# Explanation: 
# operation = `[[0, 2], [1, 5], [0, 9], [2, 15]]`
# At 0-th second, the lamps will accept the operation `[0, 2]`, so the lamp0 will turn on, and it will turn off at the 2-nd second.It will lighting `2-0 = 2` seconds.
# At 2-nd second, the lamps will accept the operation `[1, 5]`, so the lamp1 will turn on, and it will turn off at the 5-th second.It will lighting `5-2 = 3` seconds.
# At 5-th second, the lamps will accept the operation `[0, 9]`, so the lamp0 will turn on, and it will turn off at the 9-th second.It will lighting `9-5 = 4` seconds.
# At 9-th second, the lamps will accept the operation `[2, 15]`, so the lamp2 will turn on, and it will turn off at the 15-th second.It will lighting `15-9 = 6` seconds.
# So the longest continuously lighting time is `max(2, 3, 4, 6) = 6` seconds.

# **You need to return a lowercase letter instead of a number, such as `'a' = 0, 'b' = 1, ..., 'z' = 25`.**
# So the answer to the above example is 'c'.

from typing import (
    List,
)

# T: O(n); S: O(1)

class Solution:
    """
    @param operation: A list of operations.
    @return: The lamp has the longest liighting time.
    """
    def longest_lighting_time(self, operation: List[List[int]]) -> str:
        # write your code here
        lighting_stats = [0 for _ in range(26)] # on/off, prev op time, longest continuous lighting time 
        prev_t = 0
        for l, t in operation:
            if t - prev_t > lighting_stats[l]:
                lighting_stats[l] = t - prev_t
            prev_t = t
        print(lighting_stats)
        idx, max_time = None, None
        for (i, t) in enumerate(lighting_stats):
            if max_time is None or max_time < t:
                idx = i
                max_time = t
        return chr(ord('a') + idx)

# TODO: No need to declare an array for all the lights.
