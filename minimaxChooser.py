import random

class MinimaxChooser: 
	def choose_move(self, engine):
		board = engine.board
		bestScore = float('-inf')
		bestMove = None
		# simulate each possible top move here, call minimax for the remaining depth,
		# then undo the simulated move and restore engine state
		for col in range(board.board_size):
			if board.board[0][col] == 0:
				# simulate move for current player and store state to restore later
				prev_last = engine.last_move
				prev_player = engine.player
				engine.simulatePlacePiece(col)

				# switch to opponent for the recursive search
				engine.player = 2 if engine.player == 1 else 1
				score = self.minimax(engine, 3, False, prev_player)

				# restore player and undo simulated move
				engine.player = prev_player
				for row in range(engine.board.board_size):
					if engine.board.board[row][col] != 0:
						engine.board.board[row][col] = 0
						break
				engine.last_move = prev_last

				if score > bestScore:
					bestScore = score
					bestMove = col

		return bestMove
		
	def minimax(self, engine, depth, maximizing_player, orig_player=None):
		# orig_player is the player who initiated the search (used for evaluation)
		if orig_player is None:
			orig_player = engine.player

		# base case
		if depth == 0 or engine.checkWin() or engine.checkTie():
			# i am truly sorry for the line of code you are about to see
			return self.evaluateBoard(engine, orig_player) + 10000 if engine.checkWin() and engine.last_move == orig_player else self.evaluateBoard(engine, orig_player) - 10000 if engine.checkWin() else self.evaluateBoard(engine, orig_player)

		if maximizing_player:
			max_eval = float('-inf')
			for col in range(engine.board.board_size):
				if engine.board.board[0][col] == 0:
					# simulate move for whoever is currently set in engine.player
					prev_last = engine.last_move
					prev_player = engine.player
					engine.simulatePlacePiece(col)

					# switch player for next eval
					engine.player = 2 if engine.player == 1 else 1
					eval = self.minimax(engine, depth - 1, False, orig_player)

					# restore player and undo the move
					engine.player = prev_player
					for row in range(engine.board.board_size):
						if engine.board.board[row][col] != 0:
							engine.board.board[row][col] = 0
							break
					engine.last_move = prev_last

					max_eval = max(max_eval, eval)
			return max_eval
		else:
			min_eval = float('inf')
			for col in range(engine.board.board_size):
				if engine.board.board[0][col] == 0:

					# simulate move for whoever is currently set in engine.player
					prev_last = engine.last_move
					prev_player = engine.player
					engine.simulatePlacePiece(col)

					# switch player for next eval
					engine.player = 2 if engine.player == 1 else 1
					eval = self.minimax(engine, depth - 1, True, orig_player)

					# undo the move and restore player
					engine.player = prev_player
					for row in range(engine.board.board_size):
						if engine.board.board[row][col] != 0:
							engine.board.board[row][col] = 0
							break
					engine.last_move = prev_last

					min_eval = min(min_eval, eval)
			return min_eval
	
	# TODO: account for 3/4 groupings (ex 2 then space then 1), blocking opponent 3/4 groupings, central column control
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
