#There are N children standing in a line. Each child is assigned a rating value.
#You are giving candies to these children subjected to the following requirements:
#Each child must have at least one candy.
#Children with a higher rating get more candies than their neighbors.
#What is the minimum candies you must give?

#Example:
#Given ratings = [1, 2], return 3.
#Given ratings = [1, 1, 1], return 3.
#Given ratings = [1, 2, 2], return 4. ([1,2,1]).

#Method: Forward-backward.
class Solution:
    # @param {int[]} ratings Children's ratings
    # @return {int} the minimum candies you must give
    def candy(self, ratings):
        if ratings == None:
            return 0
        lr = len(ratings)
        if lr == 0:
            return 0
        candies = [1]
        for i in xrange(1, lr):
            if ratings[i] > ratings[i - 1]:
                candies.append(candies[-1] + 1)
            else:
                candies.append(1)
        for i in range(1, lr)[::-1]:
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)
        return sum(candies)
