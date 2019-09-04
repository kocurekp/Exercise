stocks = (9, 11, 8, 5, 7, 10)
stack = []
buy = None
sell = None
maxValue = -1

for x in stocks:
	if buy == None:
		buy = x
		continue
	if sell == None:
		if buy != None:
			sell = x
	if x < buy:
		amount = [buy,sell]
		stack.append(amount)
		buy = x
		sell = None
		continue
	if x > sell:
		sell = x

amount = [buy,sell]
stack.append(amount)

for x in stack:
	value = x[1]-x[0]
	if value > maxValue:
		maxValue = value

print(maxValue)
