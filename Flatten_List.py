#Given a list, each element in the list can be a list or integer. flatten it into a simply list with integers.

#Notice
#If the element in the given list is a list, it can contain list too.

#Example
#Given [1,2,[1,2]], return [1,2,1,2].
#Given [4,[3,[2,[1]]]], return [4,3,2,1].

#There are some problems with the test cases on Lintcode. The problem says "given a list", but two test cases are integers (10, 189).

class Solution(object):
  # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        res = []
        for x in nestedList:
            if type(x) != int:
                res += self.flatten(x)
            else:
                res.append(x)
        return res
