keyboard = {2:["a", "b", "c"], 3: ["d", "e", "f"]}
print(keyboard)
num = "23"
stack = []
string = []

for number in num:
	key = int(number)
	if key in keyboard:
		stack.append(keyboard[key])

while stack:
	temp = stack.pop()
	if not string:
		string = temp
		continue
	string = zip(temp, string)

	print(list(string))
