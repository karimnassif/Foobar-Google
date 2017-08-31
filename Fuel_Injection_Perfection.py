#Commander Lambda has asked for your help to refine the automatic quantum antimatter 
#fuel injection system for her LAMBCHOP doomsday device. 
#It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a 
#bit of sabotage while you're at it - so you took the job gladly. 

#Quantum antimatter fuel comes in small pellets, 
#which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time.
#However, minions dump pellets in bulk into the fuel intake. Y
#ou need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

#The fuel control mechanisms have three operations: 

#1) Add one fuel pellet
#2) Remove one fuel pellet
#3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a 
#	quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if 
#	there is an even number of pellets)

#Write a function called answer(n) which takes a positive integer as a string and returns the minimum number of operations needed to 
#transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, 
#so there won't ever be more pellets than you can express in that many digits.

#For example:
#answer(4) returns 2: 4 -> 2 -> 1
#answer(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1


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