#Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

#Example
#Given the following triangle:

#[
#     [2],
#    [3,4],
#   [6,5,7],
#  [4,1,8,3]
#]
#The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

#Note
#Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

#Clearly use dynamic programming. To obtain O(1) space, we can actually directly modify the original array, but this may not be allowed.

#Method 1: Top-down
class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        if triangle == []:
            return 0
        prev = triangle[0]
        for row in triangle[1:]:
            cur = [row[0] + prev[0]]
            for i in xrange(1, (len(row) - 1)):
                cur.append(row[i] + min(prev[i - 1], prev[i]))
            cur.append(row[-1] + prev[-1])
            prev = cur
        return min(prev)
