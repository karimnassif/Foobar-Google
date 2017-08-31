def answer(n):
	current = int(n)
	steps = 0


	while current != 1:
		#When even, always divide by 2
		if current%2 == 0:
			current /= 2
		#3 is an exception to rules used and thus hardcoded
		elif current == 3:
			current -= 1
		#If odd, check if either neighbour is a power of 2
		elif current%2 == 0 and isPower2(current+1) == True:
			current+=1
		elif current%2 == 0 and isPower2(current-1) == True:
			current-=1
		#If neither neighbour is a power of 2, the best option
		#is the one with the least trailing 0's
		else:
			tz_a=trailing_zeros(current+1)
			tz_b=trailing_zeros(current-1)
			if tz_a>tz_b:
				current+=1
			else:
				current-=1
		steps+=1
	return steps

#Function to find trailing 0's
def trailing_zeros(x):
    count = bin(x)[2:]
    return len(count)-len(count.rstrip('0'))

#Function to determine if power of 2
def isPower2(n):
	if n!=0:
		return n != 0 and ((n & (n - 1)) == 0)

print answer(15)