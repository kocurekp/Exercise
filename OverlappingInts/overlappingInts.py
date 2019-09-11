intervals = [(1,3),(5,8),(4,10), (20,25)]
stack = []
start = None
length = len(intervals)
print(intervals)
print()
i = 0
x = 0
y = 1

while True:
	if intervals[x][0] > intervals[y][0]:
		i = 0
		temp = intervals[y]
		intervals[y] = intervals[x]
		intervals[x] = temp

	if i >= length:
		break

	if y == length - 1:
		x = 0
		y = 1

	else:
		x += 1
		y += 1

	i += 1

#merge

j = 0
k = 1

while k < len(intervals):
	if intervals[j][1] > intervals[k][0]:
		if intervals[j][1] > intervals[k][1]:
			merged = (intervals[j][0], intervals[j][1])
		else:
			merged = (intervals[j][0], intervals[k][1])

		intervals[j] = "X"
		intervals[k] = merged
	j += 1
	k += 1

for x in intervals:
	if x == "X":
		intervals.remove(x)
		
print(intervals)