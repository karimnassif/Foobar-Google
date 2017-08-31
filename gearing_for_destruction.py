def answer(pegs):
	first = pegs[0]
	sign = -1
	arrLen = len(pegs)
	for peg in pegs:
		first += peg*sign*2
		sign *= -1
	first += pegs[arrLen-1] * sign
	first *= 2
	divisor = 3 if arrLen%2==0 else 1
	if first%divisor==0:
		first /= divisor
		divisor = 1

	lastRadius = first/divisor
	for x in xrange(arrLen-1):
		width = pegs[x+1]-pegs[x]
		if lastRadius < 0 or lastRadius > (width-1):
			return [-1, -1]
		lastRadius = width - lastRadius

	return [first, divisor]


test = [4, 17, 50]
print answer(test)
