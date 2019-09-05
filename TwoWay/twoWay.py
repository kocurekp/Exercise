matrix = [['F', 'A', 'c', 'I'],['O', 'B', 'Q', 'P'],['A', 'N', 'O', 'B'], ['M', 'A', 'S', 'S']]

target = 'FOAM'

for x in matrix:
	print(x)

def UpToDown(i, j):
	m = i
	k = 0
	while k < len(target):
		try:
			if matrix[m][j] == target[k]:
				k += 1
				m += 1
			else:
				break
		except IndexError:
			break

	if k == len(target):
		print("found up to down")

def LeftToRight(i, j):
	m = j
	k = 0
	while k < len(target):
		try:
			if matrix[i][m] == target[k]:
				k += 1
				m += 1
			else:
				break
		except IndexError:
			break
	if k == len(target):
		print("found left to right")

def FindTarget():
	i = 0
	j = 0
	while i < len(matrix):
		while j < len(matrix[0]):
			if matrix[i][j] == target[0]:
				UpToDown(i,j)
				LeftToRight(i,j)
			j += 1
		j = 0
		i +=1

print(target)
FindTarget()




