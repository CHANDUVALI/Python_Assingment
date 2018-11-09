#Implement a program to find the square root of a function using newton-rapson method.

def square_root(n):
	# use n itself as initial approximation
	x = n 
	y = 1
	# e decides accuracy level
	e = 0.000000000000001

	while(x-y > e):
		x = (x+y)/2
		y = n/x
	return x

n = int(input("Enter a number"))
print(" Square root is: \n", square_root(n))


