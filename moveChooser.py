import random

class MoveChooser: 
	def choose_move(self, engine):
		board = engine.board
		current_player = engine.player
		last_move = engine.last_move
		
		if last_move and board.board[0][last_move] == 0:
			return last_move
		else:
			found = False
			while not found: 
				col = random.randint(0, board.board_size - 1)
				if board.board[0][col] == 0:
					found = True
					return col
