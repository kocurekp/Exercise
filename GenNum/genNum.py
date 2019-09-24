import random
n = 5
l = [2,3,4]

def Generate(n, l):
	a = random.randrange(0,n)
	for item in l:
		if item == a:
			a = Generate(n,l)
	return a

for x in range(1,20):
	result = Generate(n,l)
	print(result)