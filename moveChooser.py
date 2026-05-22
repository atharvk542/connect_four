import random

class MoveChooser: 
	def choose_move(self, engine):
		board = engine.board
		current_player = engine.player
		last_move = engine.last_move
		if engine.player == 1:
			return random.randint(0, engine.board_size - 1)
		else:
			return random.randint(0, engine.board_size - 1)