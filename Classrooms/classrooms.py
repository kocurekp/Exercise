i = 0
arr = []
interval = []

while 1:
	user_input_start = int(input("enter start of the interval: "))
	user_input_end = int(input("enter end of the interval: "))

	interval = [user_input_start, user_input_end]
	arr.append(interval)

	input_next = input("quit? ('q')")

	if input_next == 'q':
		break
	else:
		continue

a = None
b = None

count = 0

i = 1
for x in arr:
	while i < len(arr):
		if x[1] < arr[i][0]:
			i += 1
			continue
		else:
			count += 1
		i += 1

print(count)