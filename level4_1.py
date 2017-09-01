from fractions import gcd

class Guard:
	def __init__(self, bananas):
		self.bananaCount = bananas
		self.infinite = []
		self.ends = []


def is_forever(x, y):
    z = (x + y) / gcd(x, y)
    return bool((z - 1) & z)

def answer(banana_list):
	length = len(banana_list)
	guards=[None]*length
	for x in xrange(length):
		guards[x]=Guard(banana_list[x])

	for x in xrange(length):
		for y in xrange(length):
			if is_forever(banana_list[x], banana_list[y]):
				guards[x].infinite.append(banana_list[y])

	guards.sort(key=lambda x: len(x.infinite))
	for x in xrange(length):
		print guards[x].bananaCount, guards[x].infinite


answer([1,7,3,21,13,19])

