# Lintcode 1871//Easy//Google

# Description
# Give you a 24-hour time (00: 00-23: 59), where one or more numbers of the four numbers are question marks. Question mark can be replaced with any number, then what is the maximum time you can represent.

# Example
# Example 1:

# Input: 
# time = "2?:00"
# Output: 
# "23:00"
# Example 2:

# Input: 
# time = "??:??"
# Output: 
# "23:59"

# T: O(1); S: O(1)

class Solution:
	"""
	@param time: a string of Time
	@return: The MaximumMoment
	"""
	def maximum_moment(self, time: str) -> str:
     	# Write your code here.
		time = list(time)
		if time[4] == '?':
			time[4] = '9'
		if time[3] == '?':
			time[3] = '5'
		if time[0] == '?' and time[1] == '?':
			return '23:'+time[3]+time[4]
		if time[0] == '?': # time[1] != '?'
			if time[1] <= '3':
				time[0] = '2'
			else:
				time[0] = '1'	
		elif time[1] == '?':
			if time[0] == '2':
				time[1] = '3'
			else:
				time[1] = '9'
		return ''.join(time)
