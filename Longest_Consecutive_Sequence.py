# Leetcode 128//Medium
# Lintcode 124//Medium
#Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

#Clarification
#Your algorithm should run in O(n) complexity.

#Example
#Given [100, 4, 200, 1, 3, 2],
#The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

#First solution: O(nlogn)
#Sort the original list. Note that there are 3 cases when comparing with previous number: prev + 1, prev, others. It's easy to leave out prev.
class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # write your code here
        num = sorted(num)
        glob, local, prev = 0, 0, None
        for n in num:
            if prev == None:
                local = 1
            elif n == prev + 1:
                local += 1
            elif n == prev:
                continue
            else:
                glob = max(glob, local)
                local = 1
            prev = n
        glob = max(glob, local)
        return glob

#Second solution: T: O(n); S: O(n)
#Use hashtable. This will first eliminate duplicated numbers and leave only distinct numbers.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums) # ensures uniqueness
        num_to_cluster = dict()
        clusters = [] # min-max clusters
        n_clusters = 0
        for n in nums:
            # merge的时候需要考虑[n, n]这种情况
            if n - 1 in num_to_cluster and n + 1 in num_to_cluster: #merge two clusters
                left = num_to_cluster[n-1]
                right = num_to_cluster[n+1]
                clusters[left][1] = clusters[right][1]
                if clusters[left][0] != n - 1:
                    num_to_cluster.pop(n-1)
                if clusters[left][1] != n + 1:
                    num_to_cluster.pop(n+1)
                num_to_cluster[clusters[left][1]] = left
            elif n - 1 in num_to_cluster:
                left = num_to_cluster[n-1]
                clusters[left][1] = n
                if clusters[left][0] != n - 1:
                    num_to_cluster.pop(n-1)
                num_to_cluster[n] = left
            elif n + 1 in num_to_cluster:
                right = num_to_cluster[n+1]
                clusters[right][0] = n
                if clusters[right][1] != n + 1:
                    num_to_cluster.pop(n+1)
                num_to_cluster[n] = right
            else:
                clusters.append([n, n])
                num_to_cluster[n] = n_clusters
                n_clusters += 1
        return max([c[1] - c[0] + 1 for c in clusters])
 
# TODO：精简code
