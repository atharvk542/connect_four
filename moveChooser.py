import random

class MoveChooser: 
	def choose_move(self, engine):
		board = engine.board
		current_player = engine.player
		last_move = engine.last_move
		
		bestScore = float('-inf')
		bestMove = None
		for col in range(board.board_size):
			if board.board[0][col] == 0:
				score = self.minimax(engine, 4, True)
				if score > bestScore:
					bestScore = score
					bestMove = col
		
		return bestMove
		
	def minimax(self, engine, depth, maximizing_player):
		if depth == 0 or engine.checkWin() or engine.checkTie():
			return self.evaluateBoard(engine, engine.player)

		if maximizing_player:
			max_eval = float('-inf')
			for col in range(engine.board.board_size):
				if engine.board.board[0][col] == 0:
					engine.simulatePlacePiece(col)
					eval = self.minimax(engine, depth - 1, False)
					max_eval = max(max_eval, eval)
					# undo the move
					for row in range(engine.board.board_size):
						if engine.board.board[row][col] != 0:
							engine.board.board[row][col] = 0
							break
			return max_eval
		else:
			min_eval = float('inf')
			for col in range(engine.board.board_size):
				if engine.board.board[0][col] == 0:
					engine.simulatePlacePiece(col)
					eval = self.minimax(engine, depth - 1, True)
					min_eval = min(min_eval, eval)
					# undo the move
					for row in range(engine.board.board_size):
						if engine.board.board[row][col] != 0:
							engine.board.board[row][col] = 0
							break
			return min_eval
	
	def evaluateBoard(self, engine, player):
		boardScore = 0

		for i in range(engine.board.board_size):
			rowCounter = 1 
			for j in range(1, engine.board.board_size):
				if engine.board.board[i][j - 1] == engine.board.board[i][j] and engine.board.	board[i][j] != 0:
						rowCounter+=1
				else:
					rowCounter = 1

				if rowCounter >= 3:
					boardScore += 10 if player == 1 else -10
				# else, boardScore += 0
		
		# cols
		for i in range(engine.board.board_size):
			colCounter = 1
			for j in range(1, engine.board.board_size):
				if engine.board.board[j - 1][i] == engine.board.board[j][i] and engine.board.board[j][i] != 0:
					colCounter+=1
				else:
					colCounter = 1

				if colCounter >= 3:
					boardScore+= 10 if player == 1 else -10
				# else:
				# 	return 0	
				
		# diagonal
		diagCounter = 1
		for i in range(1, engine.board.board_size):
			if engine.board.board[i - 1][i - 1] == engine.board.board[i][i] and engine.board.board[i][i] != 0:
				diagCounter+=1
			else:
				diagCounter = 1
			
			if diagCounter >= 3:
				boardScore += 10 if player == 1 else -10
			# else:
			# 	boardScore += 0

		# anti diagonal
		antiDiagCounter = 1
		for i in range(engine.board.board_size - 1):
			if engine.board.board[i][engine.board.board_size - i - 1] == engine.board.board[i + 1][engine.board.board_size - i - 2] and engine.board.board[i][engine.board.board_size -i - 1] != 0:
				antiDiagCounter += 1
			else:
				antiDiagCounter = 1
			
			if antiDiagCounter >= 3:
				boardScore += 10 if player == 1 else -10
			# else:
			# 	boardScore += 0
		
		return boardScore
