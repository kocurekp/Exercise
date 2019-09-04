import operator

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

tree = ["*", ["+", [3,2]],["+", [4,5]]]
opStack = []
numStack = []
results = []
isNum = False

def StoreOperator(x):
	if len(x) == 1:
		opStack.append(x)
		isNum = False
		return isNum
	else:
		isNum = True
		if isinstance(x[1][0], int):
			num = [int(x[1][0]), int(x[1][1])] 
			numStack.append(num)
			StoreOperator(x[0])	
		else:
			isNum = StoreOperator(x)
		return isNum

for item in tree:
	if StoreOperator(item):
		num = numStack.pop()
		operator = opStack.pop()
		result = ops[operator](num[0],num[1])
		results.append(result)

while opStack:
	operator = opStack.pop()
	num1 = results.pop()
	num2 = results.pop()
	result = ops[operator](num2,num1)
	results.append(result)

print(results[0])
