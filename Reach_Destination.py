# Lintcode 1855//Hard
# Description
# Given a starting point (sx, sy) and an ending point (dx, dy). If the starting point can be converted to the ending point through a series of conversions, return true, otherwise return false.
# The conversion rule is: you can transform point (x, y) to (x, x + y) or (x + y, y).

# 1<=sx,sy,dx,dy<=10^9
# Guaranteed starting point is not equal to ending point.

# Example
# Example 1:

# Input: 
# sx = 1, sy = 1, dx = 3, dy = 5
# Output: 
# True
# Explanation:
# You can do the following transformations
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
# Example 2:

# Input: 
# sx = 2, sy = 3, dx = 7, dy = 11
# Output: 
# False

# 一开始答案：DFS + visited node memorization。超出空间限制（正向传播状态太多）
class Solution:
    """
    @param sx: the start x
    @param sy: the start y
    @param dx: the destination x
    @param dy: the destination y
    @return: whether you can reach the destination
    """
    def reach_destination(self, sx: int, sy: int, dx: int, dy: int) -> bool:
        # Write your code here.
        from collections import deque
        stack = deque([(sx, sy)])
        visited_nodes = set()
        while len(stack) > 0:
            print(stack)
            cur_x, cur_y = stack.pop()
            if (cur_x, cur_y) in visited_nodes:
                continue
            visited_nodes.add((cur_x, cur_y))
            if cur_x > dx or cur_y > dy:
                continue
            if cur_x == dx and cur_y == dy:
                return True
            if cur_x + cur_y <= dy: # 注意等于号
                stack.append((cur_x, cur_x+cur_y))
            if cur_x + cur_y <= dx:
                stack.append((cur_x+cur_y, cur_y))
        return False

# 考虑一个状态下(sx', sy')的前一个状态(sx, sy)。那么sx = sx', sy = sy' - sx'，或者sx = sx' - sy'，sy = sy'
# 1. 由于sx > 0, sy > 0，无论取(sx, sx+sy)或者(sx+sy, sy)都必有sx' != sy'（前者sx' < sy'，后者sx' > sy'）。因此只可能初始态设置了x、y相等，在后面的sequence里不能出现x、y相等。
# 2. 如果sx' < sy'，则必须sx = sx', sy = sy' - sx'，否则sx < 0。
# 3. 如果sx' > sy'，则必须sx = sx' - sy', sy = sy'，否则sy < 0。
# 第二次答案recursion。仍通过不了
class Solution:
    """
    @param sx: the start x
    @param sy: the start y
    @param dx: the destination x
    @param dy: the destination y
    @return: whether you can reach the destination
    """
    def reach_destination(self, sx: int, sy: int, dx: int, dy: int) -> bool:
        # Write your code here.
        if sx == dx and sy == dy:
            return True
        if dx == dy:
            return False
        if dx < sx or dy < sy:
            return False
        if dx > dy:
            return self.reach_destination(sx, sy, dx-dy, dy)
        return self.reach_destination(sx, sy, dx, dy-dx)

# 最终解
class Solution:
    """
    @param sx: the start x
    @param sy: the start y
    @param dx: the destination x
    @param dy: the destination y
    @return: whether you can reach the destination
    """
    def reach_destination(self, sx: int, sy: int, dx: int, dy: int) -> bool:
        # Write your code here.
        while dx >= sx and dy >= sy:
            if sx == dx and sy == dy:
                return True
            if dx == dy:
                return False
            if dx == sx:
                return (dy - sy) % dx == 0
            if dy == sy:
                return (dx - sx) % dy == 0
            if dx > dy:
                dx = dx % dy
            else:
                dy = dy % dx
        return False



