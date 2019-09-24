import random
n = int(input("integer: "))
l = []
listLength = int(input("length of list: "))

for x in range(0,listLength):
	num = int(input("Number to add to list: "))
	l.append(num)
print(l)
def Generate(n, l):
	a = random.randrange(0,n)
	for item in l:
		if item == a:
			a = Generate(n,l)
	return a

for x in range(0,20):
	result = Generate(n,l)
	print(result)