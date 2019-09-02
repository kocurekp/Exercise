# string = "([])"
string = input("String of brackets to be checked (returns True if the brackets are well-formed): ")
previousChar = None
correct = None
stack = []

roundOpen = 0
roundClosed = 0
curlyOpen = 0
curlyClosed = 0
squareOpen = 0
squareClosed = 0

def fail(e):
	# print(e)
	print(False)
	exit(1)

for char in string:
	if char == "(":
		if roundClosed > roundOpen:
			fail("round open")
		else:
			roundOpen += 1
	elif char == "{":
		if curlyClosed > curlyOpen:
			fail("curly open")
		else:
			curlyOpen += 1
	elif char == "[":
		if squareClosed > squareOpen:
			fail("square open")
		else:
			squareOpen += 1
	elif char == ")":
		if roundClosed < roundOpen:
			previousChar = stack.pop()
			if previousChar == "(":
				roundClosed += 1
				continue
			else:
				fail("round prev")
		else:
			fail("round closed")
	elif char == "}":
		if curlyClosed < curlyOpen:
			previousChar = stack.pop()
			if previousChar == "{":
				curlyClosed += 1
				continue
			else:
				fail("curly prev")
		else:
			fail("curly closed")
	elif char == "]":
		if squareClosed < squareOpen:
			previousChar = stack.pop()
			if previousChar == "[":
				squareClosed += 1
				continue
			else:
				fail("square prev")
		else:
			fail("square closed")

	stack.append(char)


if roundOpen == roundClosed and curlyOpen == curlyClosed and squareOpen == squareClosed:
	print(True)
else:
	fail("wrong")