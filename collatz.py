def collatz(number):
	if number % 2 == 0:     #number is even
		result = (number // 2)
		print(result)
		return(result)
	else:                   #number is odd
		result = (3 * number + 1)
		print(result)
		return(result)
		
print ('Type in a number: ')
try:
	number = int(input())  # number is what the user enters
	while number != 1:
		number = collatz(int(number))
except ValueError:
	print ('Please type in a valid integer')

