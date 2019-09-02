
# returns remaining distance to final destination
def CountDistance(currentRow, currentColumn):
	return abs(currentRow - endRow)+abs(currentColumn - endColumn)
	
# prints position, distance to destination
def PrintDistance():
	distance = CountDistance(currentRow, currentColumn)
	print("Position: ("+str(currentRow)+","+str(currentColumn)+")")
	print("Distance: "+str(distance))
	if (currentRow == endRow) and (currentColumn == endColumn):
		MarkVisited(currentRow, currentColumn)
		print("End: ("+str(currentRow)+","+str(currentColumn)+")")
		print("found in "+str(steps)+" steps")
		exit(0)

# returns False if next position is not out of range
def Failed(currentRow, currentColumn):
	if (currentRow < 0)	or (currentColumn < 0): 
		return True
	else:
		if (len(matrix[0]) - currentColumn) > 0:
			if  (len(matrix) - currentRow) > 0:
				return False
			else:
				return True
		else:
			return True

# marks visited position
def MarkVisited(currentRow,currentColumn):
	matrix[currentRow][currentColumn] = 5
	x=0
	while x < len(matrix):
		print(matrix[x])
		x +=1
	position = [currentRow, currentColumn]
	visited.append(position)

# counts distance to final destination in case of moving up
def UpDistance(currentRow, currentColumn):
	up = 999
	currentRow -= 1
	if Failed(currentRow, currentColumn):
		currentRow += 1
	else:
		if (matrix[currentRow][currentColumn]):
			pass
		else:
			up = CountDistance(currentRow, currentColumn)
			currentRow += 1
	return up

# counts distance to final destination in case of moving right
def RightDistance(currentRow, currentColumn):
	right = 999
	currentColumn += 1
	if Failed(currentRow, currentColumn):
		currentColumn -= 1
	else:
		if (matrix[currentRow][currentColumn]):
			pass
		else:
			right = CountDistance(currentRow, currentColumn)
			currentColumn -= 1
	return right

# counts distance to final destination in case of moving down
def DownDistance(currentRow, currentColumn):
	down = 999
	currentRow += 1
	if Failed(currentRow, currentColumn):
		currentRow -= 1
	else:
		if (matrix[currentRow][currentColumn]):
			pass
		else:
			down = CountDistance(currentRow, currentColumn)
			currentRow -= 1
	return down

# counts distance to final destination in case of moving left
def LeftDistance(currentRow, currentColumn):
	left = 999
	currentColumn -= 1
	if Failed(currentRow, currentColumn):
		currentRow += 1
	else:
		if (matrix[currentRow][currentColumn]):
			pass
		else:
			left = CountDistance(currentRow, currentColumn)
			currentRow += 1
	return left

# add possible directions to stack
def StorePosition(currentRow, currentColumn, directions):
	wrongDirections = directions.count(999)
	if wrongDirections < 4:
		pos = [currentRow, currentColumn, directions]
		stack.append(pos)

visited = [] # visited positions stored in case of dead end
stack = [] # visited positions with more possible directions
steps = 0 
t = 1
f = 0
matrix = [[f,f,f,f,f,f,f,f],[f,t,f,t,t,t,f,t],[f,t,t,f,f,f,t,f],[f,t,f,f,f,f,f,f],[f,f,f,f,f,f,f,f]]

#print matrix
i = 0
while i < len(matrix):
	print(matrix[i])
	i += 1

startRow = input("Starting position row (0-"+str(len(matrix)-1)+"): ")
startColumn = input("Starting position column (0-"+str(len(matrix[0])-1)+"): ")
endRow = int(input("Destination row (0-"+str(len(matrix)-1)+"): "))
endColumn = int(input("Destination column (0-"+str(len(matrix[0])-1)+"): "))

currentRow = int(startRow)
currentColumn = int(startColumn)

i = 0
while True:
	steps += 1
	i += 1

	up = UpDistance(currentRow, currentColumn)
	right = RightDistance(currentRow, currentColumn)
	down = DownDistance(currentRow, currentColumn)
	left = LeftDistance(currentRow, currentColumn)
	
	directions = [up, right, down, left]
	forbiddenDirectionsCounter = directions.count(999)

	# dead end, returning to previous crossroads
	if forbiddenDirectionsCounter == 4:
		prevCrossPos = [0] #stack with more possible directions
		prevVisited = [1] #previous visited position 

		try:	
			previousCrossroads = stack.pop()
			matrix[currentRow][currentColumn] = 5
			position = [currentRow, currentColumn]
			visited.append(position)

		except IndexError as e:
			print("End: ("+str(endRow)+","+str(endColumn)+")")
			print("dead end")
			exit(0)

		prevRow = previousCrossroads[0]
		prevCol = previousCrossroads[1]
		prevDir = previousCrossroads[2]

		prevCrossPos = [prevRow, prevCol]
		currentRow = prevCrossPos[0]
		currentColumn = prevCrossPos[1]

		matrix[currentRow][currentColumn] = 5
		position = [currentRow, currentColumn]
		visited.append(position)

		while prevCrossPos != prevVisited:
			steps += 1
			try:
				prevVisited = visited.pop()

			except IndexError as e:
				matrix[currentRow][currentColumn] = 5
				position = [currentRow, currentColumn]
				visited.append(position)

		up = prevDir[0]
		right = prevDir[1]
		down = prevDir[2]
		left = prevDir[3]

	# move to direction that is the closest to final destination, if not obvious move in order up, right, down, left 
	if (up <= right) and (up <= down) and (up <= left):
		up = 999
		directions = [up, right, down, left]
		StorePosition(currentRow, currentColumn, directions)
		MarkVisited(currentRow, currentColumn)
		currentRow -= 1
		print("up")
		PrintDistance()
		continue

	if (right <= up) and (right <= down) and (right <= left):
		right = 999
		directions = [up, right, down, left]
		StorePosition(currentRow, currentColumn, directions)
		MarkVisited(currentRow, currentColumn)
		currentColumn += 1
		print("right")
		PrintDistance()
		continue

	if (down <= up) and (down <= right) and (down <= left):
		down = 999
		directions = [up, right, down, left]
		StorePosition(currentRow, currentColumn, directions)
		MarkVisited(currentRow, currentColumn)
		currentRow += 1
		print("down")
		PrintDistance()
		continue

	if (left <= up) and (left <= right) and (left <= down):
		left = 999
		directions = [up, right, down, left]
		StorePosition(currentRow, currentColumn, directions)
		MarkVisited(currentRow, currentColumn)
		currentColumn -= 1
		print("left")
		PrintDistance()
		continue