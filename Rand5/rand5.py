import random
def Rand7():
	num = random.randrange(1,7)
	return num

def Rand5():
	num = 0
	while (num < 1 or num > 5):
		num = Rand7()
	return num

print(Rand5())