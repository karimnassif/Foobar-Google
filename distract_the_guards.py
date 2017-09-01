from fractions import gcd

#Class to keep track of each guard and the pairs they infinitely loop with
class Guard:
	def __init__(self, bananas):
		self.bananaCount = bananas
		self.infinite = []


#Tests if two guards will loop infinitely
def is_forever(x, y):
    z = (x + y) / gcd(x, y)
    return bool((z - 1) & z)

def answer(Banana_list):
    banana_list = sorted(Banana_list)
    length = len(banana_list)
    guards=[None]*length
    pairs = 0

    for x in xrange(length):
    	guards[x]=Guard(banana_list[x])
    
 	#Finding the matching pairs of each guard	
    for x in xrange(length):
    	for y in xrange(length):
    		if is_forever(banana_list[x], banana_list[y]):
    			guards[x].infinite.append(banana_list[y])

    #Sorting guards by least amount of pairs. 
    guards.sort(key=lambda x: len(x.infinite))

    #While not perfect, by matching guards starting with those who have
    #the least amount of possible pairs, a good approximation is reached
    #as to the combinations that result in the most paired guards.
    for x in xrange(0, length):
    	for y in xrange(length-1, 1, -1):
    		if guards[x].bananaCount in guards[y].infinite and guards[y].bananaCount in guards[x].infinite:
    			pairs +=1 
    			guards[x].infinite = []
    			guards[y].infinite = []
    return length-(pairs*2)