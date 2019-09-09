stack = [-10, -10, 5, 2]
highestMul = None
for x in range(0,len(stack)):
	for y in range(1,len(stack)):
		for z in range(2,len(stack)):
			mul = stack[x] * stack[y] * stack[z]
			if not highestMul:
				highestMul = mul
			elif mul > highestMul:
				highestMul = mul
print(highestMul)