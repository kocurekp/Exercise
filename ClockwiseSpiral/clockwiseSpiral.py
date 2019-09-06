matrix = [  [1,2,3,4,5],
			[6,7,8,9,10],
			[11,12,13,14,15],
			[16,17,18,19,20],
			[21,22,23,24,25]]

for x in matrix:
	print(x)
print()

storage = []

startRow = 0
endRow = len(matrix)
startCol = 0
endCol = len(matrix[0])

valueCount = endRow * endCol

while len(storage) < valueCount:
	storeStartCol = startCol
	while startCol < endCol:
		storage.append(matrix[startRow][startCol])
		startCol += 1
	endCol = storeStartCol
	startCol -= 1
	startRow += 1

	storeStartRow = startRow
	while startRow < endRow:
		storage.append(matrix[startRow][startCol])
		startRow += 1
	endRow = storeStartRow - 1
	startRow -= 1
	startCol -= 1

	storeStartCol = startCol
	while startCol > endCol:
		storage.append(matrix[startRow][startCol])
		startCol -= 1
	endCol = storeStartCol + 1

	storeStartRow = startRow
	while startRow > endRow:
		storage.append(matrix[startRow][startCol])
		startRow -= 1
	endRow = storeStartRow
	startRow += 1
	startCol += 1

print(storage)