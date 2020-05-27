_list = [1,1,3]
sum = 3

class Test:
	def  match(self,_list,sum):
		for i in range(len(_list)):
			for j in range(i+1,len(_list)):
				if _list[i] + _list[j] == sum:
					print('match found')
					return 
		print('no match found')
	@staticmethod
	def  static_match(_list,sum):
		for i in range(len(_list)):
			for j in range(i+1,len(_list)):
				if _list[i] + _list[j] == sum:
					print('match found')
					return 
		print('no match found')


Test().static_match(_list,sum)

test = Test()	
test.match(_list,sum)

str = "I am a boy"

list = str.split().reverse()

reversestring = ' '.join(list)

print(reversestring)




