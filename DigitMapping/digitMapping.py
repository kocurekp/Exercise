keyboard = {2:["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"]}
print(keyboard)
num = "23"
stack = []
string = []
result = []
tempString = ""
tempString2 = ""

for number in num:
	key = int(number)
	if key in keyboard:
		stack.append(keyboard[key])

while stack:
	temp = stack.pop()
	if not string:
		string = temp
	else:
		for x in string:
			for y in temp:
				tempString += x.join(y)
				tempString2 += y.join(x)

for x in range(0,len(tempString)):
	result.append(tempString[x] + tempString2[x]) 

print(result)


