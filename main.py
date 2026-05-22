import random
from moveChooser import MoveChooser
class ConnectFour:
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
	board_size = 8
	board = []
	gameOver = False
	player = 1
	last_move = None

	def __init__(self, board_size):
		self.board_size = board_size
		self.board = [[0] * board_size for _ in range(board_size)]
		self.gameOver = False
		self.last_move = None

	def placePiece(self, col):
		j = col
		for i in range(self.board_size - 1, -1, -1): # iterate backwards from board_size - 1
			if self.board[i][j] == 0:
				placed_by = self.player
				self.board[i][j] = self.player
				self.player = 2 if self.player == 1 else 1
				self.last_move = (i, j, placed_by)
				return self.board
		
		return self.board

	def checkWin(self, board):
		# TODO: set counter to 0 if the current square doesn't match, otherwise '1 0 1 0 1 0 1' passes as a row
		# rows
		for i in range(self.board_size):
			rowCounter = 1 
			for j in range(1, self.board_size):
				if board[i][j - 1] == board[i][j] and board[i][j] != 0:
						rowCounter+=1
				else:
					rowCounter = 1

				if rowCounter >= 4:
					return True	
		
		# cols
		for i in range(self.board_size):
			colCounter = 1
			for j in range(1, self.board_size):
				if board[j - 1][i] == board[j][i] and board[j][i] != 0:
					colCounter+=1
				else:
					colCounter = 1

				if colCounter >= 4:
					return True	

		# diagonal
		diagCounter = 1
		for i in range(1, self.board_size):
			if board[i - 1][i - 1] == board[i][i] and board[i][i] != 0:
				diagCounter+=1
			else:
				diagCounter = 1
			
			if diagCounter >= 4:
				return True

		# anti diagonal
		antiDiagCounter = 1
		for i in range(self.board_size - 1):
			if board[i][self.board_size - i - 1] == board[i + 1][self.board_size - i - 2] and board[i][self.board_size -i - 1] != 0:
				antiDiagCounter += 1
			else:
				antiDiagCounter = 1
			
			if antiDiagCounter >= 4:
				return True

		return False

	def checkTie(self, board):
		if not self.checkWin(board):
			for i in board:
				for j in i:
					if j == 0:
						return False
			
			return True
		
		return False

	def printBoard(self, board):
		print('-'*10 + "CURRENT BOARD" + '-'*10)
		for i in range(self.board_size):
			for j in range(self.board_size):
				print(board[i][j], end=' ')

			print()
		print('-'*33)

if __name__ == "__main__":
	engine = ConnectFour(8)
	move_chooser = MoveChooser()
	while not engine.gameOver:
		print("player " + str(engine.player) + "'s turn")
		# selected_col = chooseMove(player)
		selected_col = move_chooser.choose_move(engine)
		engine.board = engine.placePiece(selected_col)
		engine.printBoard(engine.board)

		# TODO: consolidate this into a checkBoard function checking for win and tie
		win = engine.checkWin(engine.board)
		tie = engine.checkTie(engine.board)

		if win:
			winner = 2 if engine.player == 1 else 1 # have to flip since engine is already on next move
			print("player " + str(winner) + " has won")
			engine.gameOver = True
		
		if tie: 
			print("the game has tied")
			engine.gameOver = True
		
