from fractions import gcd

class Guard:
	def __init__(self, bananas):
		self.bananaCount = bananas
		self.infinite = []
		self.ends = []


def is_forever(x, y):
    z = (x + y) / gcd(x, y)
    return bool((z - 1) & z)

def answer(Banana_list):
	banana_list = sorted(Banana_list)
	length = len(banana_list)
	guards=[None]*length
	pairs = 0
	test = []
	for x in xrange(length):
		guards[x]=Guard(banana_list[x])

	for x in xrange(length):
		for y in xrange(length):
			if is_forever(banana_list[x], banana_list[y]):
				guards[x].infinite.append(banana_list[y])
			else:
				guards[x].ends.append(banana_list[y])

	guards.sort(key=lambda x: len(x.infinite))
	for x in xrange(length):
		print guards[x].bananaCount, guards[x].infinite

	for x in xrange(0, length):
		for y in xrange(length-1, 1, -1):
			if guards[x].bananaCount in guards[y].infinite and guards[y].bananaCount in guards[x].infinite:
				print guards[x].bananaCount, guards[y].bananaCount
				pairs +=1 
				guards[x].infinite = []
				guards[y].infinite = []
				test.append(guards[x].bananaCount)
				test.append(guards[y].bananaCount)
	return length-(pairs*2)
				
	print test
	print pairs

print answer([1, 7, 3, 21, 13, 19])