# string = "4A3B2C1D2A"
string = input("Enter the string to be decoded/encoded: ")
encoded = ""
counter = 0
prevChar = None
strToNum = True
value = 0

for char in string:
	if char.isnumeric():
		strToNum = False

if strToNum:
	for char in string:
		
		if prevChar == None:
			prevChar = char	
			counter += 1
			continue
		
		if char == prevChar:
			counter += 1
			continue
		else:
			encoded += str(counter)
			encoded += prevChar
			counter = 0

		prevChar = char	
		counter += 1

	encoded += str(counter)
	encoded += prevChar

else:
	for char in string:
		if char.isnumeric():
			value = int(char)
		else:
			while value > 0:
				encoded += char
				value -= 1

print(encoded)