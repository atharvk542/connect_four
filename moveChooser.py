import random

class MoveChooser: 
	def choose_move(self, engine):
		board = engine.board
		current_player = engine.player
		last_move = engine.last_move
		
		return last_move if last_move else random.randint(0, board.board_size - 1)