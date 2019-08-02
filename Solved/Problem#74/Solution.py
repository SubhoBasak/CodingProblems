def exists(board, word):
	if len(word) == 0:
		return False

	starting_points = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == word[0]:
				starting_points.append((i, j))

	if len(word) == 1 and len(starting_points) != 0:
		return True
	elif len(word) >= 2:
		for i, j in starting_points:
			x = __exists(i, j, word[1], word[2:], [(i, j)], len(board), len(board[0]))
			if x == True:
				return x
		return False

def __exists(x, y, cur, rest, used, maxX, maxY):
	if x+1 < maxX:
		if board[x+1][y] == cur and (x+1, y) not in used:
			if len(rest) == 0:
				return True
			return __exists(x+1, y, rest[0], rest[1:], used+[(x+1, y)], maxX, maxY)
	if x-1 >= 0:
		if board[x-1][y] == cur and (x-1, y) not in used:
			if len(rest) == 0:
				return True
			return __exists(x-1, y, rest[0], rest[1:], used+[(x-1, y)], maxX, maxY)
	if y+1 < maxY:
		if board[x][y+1] == cur and (x, y+1) not in used:
			if len(rest) == 0:
				return True
			return __exists(x, y+1, rest[0], rest[1:], used+[(x, y+1)], maxX, maxY)
	if y-1 >= 0:
		if board[x][y-1] == cur and (x, y-1) not in used:
			if len(rest) == 0:
				return True
			return __exists(x, y-1, rest[0], rest[1:], used+[(x, y-1)], maxX, maxY)
	return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

print(exists(board, "ABCCED"))
print(exists(board, "SEE"))
print(exists(board, "ABCB"))
