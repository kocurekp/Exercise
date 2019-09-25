class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.data = key

def FindNode(root,level,maxLevel,result):
	if root != None:
		level+=1
		FindNode(root.left, level, maxLevel,result)

		if level>maxLevel[0]:
			result[0] = root.data
			maxLevel[0] = level

		FindNode(root.right, level, maxLevel, result)

def DeepestNode(root):
	result = [-1]
	maxLevel = [-1]

	FindNode(root, 0, maxLevel, result)
	return result[0]

if __name__ == '__main__': 
    root = Node("a")
    root.left = Node("b")
    root.right = Node("c")
    root.left.left = Node("d")
    print(DeepestNode(root)) 