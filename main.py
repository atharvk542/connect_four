'''
---vars---
board = [4][4] idk how this works in python vbut ykwim
gameOver = false

---helper functions---
placePiece(col, board, player)
	given the column and the board, iterates for fixed j and i 0 through 3 board[i][j] 
	to find the first empty square, updates that, and returns the new board
	if playerone, puts a 1 there, else puts a 2

checkWin(board)
	itereates through every row, column, and diagonal/antidiagonal to check for 4 
	of a kind (either 4 1s or 4 2s) does this greedily, returns bool if a player won

printBoard(board)
	prints the board nicely 

---game loop---
while game not finished
	currentplayer = true if playerone else false (whatever ternary syntax is in python)
	player = 1

	print("player " + player + "'s turn")
	selected_col = input("select a column")
	board = placePiece(col, board, player) # this gives the new board after the move
	printBoard(board) 

	win = checkWin(board)

	player = 2 if player == 1 else player = 1 # another ternary

'''


board = [[0] * 4 for _ in range(4)]

gameOver = False

def placePiece(col, board, player):
	j = col
	for i in range(len(board) - 1, -1, -1):
		if board[i][j] == 0:
			board[i][j] = player
			return board
	
	return board

def checkWin(board):
	
	#rows
	for i in range(len(board)):
		rowSolved = True
		for j in range(1, len(board)):
			if board[i][j] == 0 or board[i][j - 1] != board[i][j]:
				rowSolved = False
				break
		
		if rowSolved:
			return True
	
	#cols
	for j in range(len(board)):
		colSolved = True
		for i in range(1, len(board)):
			if board[i][j] == 0 or board[i][j] != board[i-1][j]:
				colSolved = False
				break
		
		if colSolved:
			return True

	# diagonal
	diagSolved = True
	for i in range(len(board)):
		if board[0][0] == 0 or board[i][i] != board[0][0]:
			diagSolved = False
			break
				
	if diagSolved:
		return True
	
	# anti diagonal
	antidiagSolved = True
	for i in range(len(board)):
		if board[len(board) - 1][0] == 0 or board[i][len(board) - i - 1] != board[len(board) - 1][0]:
			antidiagSolved = False
			break
	
	if antidiagSolved:
		return True

	return False

def printBoard(board):
	print('-'*10 + "CURRENT BOARD" + '-'*10)
	for i in range(len(board)):
		for j in range(len(board)):
			print(board[i][j], end=' ')

		print()
	print('-'*33)

player = 1
while not gameOver:
	print("player " + str(player) + "'s turn")
	selected_col = int(input("select a column (please be nice. put something 1 to 4 in)")) - 1
	board, _ = placePiece(selected_col, board, player)
	printBoard(board)
	win = checkWin(board)

	if win:
		print("player " + str(player) + " has won")
		gameOver = True
	
	player = 2 if player == 1 else 1