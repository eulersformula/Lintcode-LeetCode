# Lintcode 1870//Medium

# Description
# Given a string str containing only 0 or 1, please return the number of substrings that consist of 0 .

# 1<=|str|<=30000

# Example
# Example 1:

# Input:
# "00010011"
# Output:
# 9
# Explanation:
# There are 5 substrings of "0",
# There are 3 substrings of "00",
# There is 1 substring of "000".
# So return 9
# Example 2:

# Input:
# "010010"
# Output:
# 5

#TODO: use for loop to iterate through the string for O(1) space compexity

class Solution:
	"""
	@param str: the string
	@return: the number of substrings 
	"""
	def string_count(self, str: str) -> int:
     	# Write your code here.
		count_n_zeros = dict()
		split_str = str.split('1')
		for sub_str in split_str:
			if sub_str.startswith('0'):
				if len(sub_str) not in count_n_zeros:
					count_n_zeros[len(sub_str)] = 0
				count_n_zeros[len(sub_str)] += 1
		res = 0
		for (k, v) in count_n_zeros.items():
			res += k * (k + 1) // 2 * v
		return res

# Space Complexity: O(n) [needs to store the split array]; Time Complexity: O(n)
