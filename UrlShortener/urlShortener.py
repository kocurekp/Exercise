import random
url = "FMfcgxwDqngTskpfQmpzfQZDhSXpKWXz"
storage = []

def Exists(url):
	for x in storage:
		if x[1] == url:
			return True
	return False

def Shorten(url):
	if not Exists(url):
		shorted = Generate()
		pair = [shorted, url]
		storage.append(pair)

def Restore(short):
	for x in storage:
		if x[0] == short:
			return x[1]

def RandomAlphaNumeric():
	number = random.randrange(48, 122)
	while not (number <= 57 or (number >= 65 and number <= 90) or number >= 97):
		number = random.randrange(48, 122)
	return number


def Generate():
	generated = ""
	while len(generated) < 6:
		number = RandomAlphaNumeric()
		generated += chr(int(number))
	return generated

#48-57, 65-90, 97-122 

Shorten(url)
print(storage)
restored = Restore(storage[0][0])
print(restored)