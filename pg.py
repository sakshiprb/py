# Given an array of integers, find two numbers such that they add up to a specific target number.
_list = [1,1,3]
sum = 3

class Test:
	@staticmethod
	def  static_match(_list,sum):
		for i in range(len(_list)):
			for j in range(i+1,len(_list)):
				if _list[i] + _list[j] == sum:
					print('match found')
					return 
		print('no match found')


Test().static_match(_list,sum)


#Reverse words in a string
str = "I am a boy"

list = str.split()
list.reverse()

reversestring = ' '.join(list)

print(reversestring)




