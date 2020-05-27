'''str = "Madam"
str1 = str.lower()
print(str1[::-1])
if str1 == str1[::-1] :
	print("Palindrome ")
else:
	print("Not Palindrome")



class Test():

	@staticmethod
	def palindrome(str1):
		i = 0
		j = len(str1)-1
		while i < j:
			if str1[i] == str1[j] : 
				i += 1
				j -= 1
			else:
				print('non Palindrome')
				return

		print('Palindrome')


print('second prog')
Test().palindrome(str1)

str = 'gjhghjh'

needle = 'jj'
print('needle found')
count = 0

for key,value in enumerate(str):
	print(key,' ', value)
	if (str[key] == needle[0] and str[key+1] == needle[1]):
		count += 1


print('count',count)

num = '123'
val = type(int(num))

if val is int:
	print(int(num))

#print(num.isnumeric())
'''
# check string is valid number or not
class test:
	@staticmethod
	def numcheck(n):
		try:
			float(n)	#checks decimal, integer, negative numbers and "exponent part"
			print ("numcheck valid number")

		except:
			print('not valid')

test().numcheck("1e10")




