#Given an array of integers, find two numbers such that they add up to a specific target number.
#The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

#Notice: You may assume that each input would have exactly one solution.

#Example: 
#numbers=[2, 7, 11, 15], target=9
#return [1, 2]

#Challenge: 
#Either of the following solutions are acceptable:
#O(n) Space, O(nlogn) Time
#O(n) Space, O(n) Time

#Method 1: Using hash map. Space Complexity: O(n), Time Complexity: O(n).
class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        rec = dict()
        for (i, n) in enumerate(numbers):
            if target - n in rec: #updating hash table and searching for result in the same run.
                return [rec[target - n] + 1, i + 1]
            rec[n] = i

#Method 2: Sorting and binary search. Space Complexity: O(n). Time Complexity: O(nlog(n)).
