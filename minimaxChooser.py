import random
from chooser import Chooser

class MinimaxChooser(Chooser): 
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

				# switch to opponent for minimax
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
	
	# TODO: add central column control, and bonus/negatives for playable on left or right
	def evaluateBoard(self, engine, player):
		boardScore = 0
		# horizontal
		for row in range(engine.board.board_size):
			for col in range(engine.board.board_size - 3):
				coords = [(row, col + i) for i in range(4)]
				window = [engine.board.board[r][c] for r, c in coords]
				boardScore += self.evaluateWindow(engine, window, coords, player)

		# vertical
		for col in range(engine.board.board_size):
			for row in range(engine.board.board_size - 3):
				coords = [(row + i, col) for i in range(4)]
				window = [engine.board.board[r][c] for r, c in coords]
				boardScore += self.evaluateWindow(engine, window, coords, player)

		# diagonal
		for row in range(engine.board.board_size - 3):
			for col in range(engine.board.board_size - 3):
				coords = [(row + i, col + i) for i in range(4)]
				window = [engine.board.board[r][c] for r, c in coords]
				boardScore += self.evaluateWindow(engine, window, coords, player)

		# anti-diagonal
		for row in range(3, engine.board.board_size):
			for col in range(engine.board.board_size - 3):
				coords = [(row - i, col + i) for i in range(4)]
				window = [engine.board.board[r][c] for r, c in coords]
				boardScore += self.evaluateWindow(engine, window, coords, player)

		return boardScore
		
	def evaluateWindow(self, engine, window, coords, player):
		score = 0
		opp_player = 2 if player == 1 else 1
		empty_count = window.count(0)
		playable_empty = self.window_has_playable_empty(engine, coords)

		# if the window has empty cells but none can be played soon, don't overvalue it
		if empty_count > 0 and not playable_empty:
			return 0

		if window.count(player) == 4:
			score += 10000
		elif window.count(player) == 3 and window.count(0) == 1:
			score += 5000
		elif window.count(player) == 2 and window.count(0) == 2:
			score += 1000

		if window.count(opp_player) == 3 and window.count(0) == 1:
			score -= 5000
		elif window.count(opp_player) == 4:
			score -= 10000

		return score
	
	def is_playable(self, engine, row, col):
		size = engine.board.board_size

		if engine.board.board[row][col] != 0:
			return False

		return row == size - 1 or engine.board.board[row + 1][col] != 0


	def window_has_playable_empty(self, engine, coords):
		for row, col in coords:
			if engine.board.board[row][col] == 0 and self.is_playable(engine, row, col):
				return True
		return False

