'''
DS: use a hashmap
Logic: 

    Store the values
    check the count
    if (count>1):
        we shud be not considering it
    we shud consider only the one which is fist occing with value one.
'''
class Solution:
	def firstUniqChar(self, s: str) -> int:

		frequency = {}

		for char in s:

			if char not in frequency:
				frequency[char] = 1
			else:
				frequency[char] = frequency[char] + 1

		for index in range(len(s)):

			if frequency[s[index]] == 1:
				return index

		return -1

            
        
        