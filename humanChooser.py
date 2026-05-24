import pygame
from chooser import Chooser

class HumanChooser(Chooser):
    def choose_move(self, engine):
        square_size = engine.screen.get_width() // engine.board.board_size

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:                
                    x, _ = pygame.mouse.get_pos()
                    if x // square_size < engine.board.board_size and engine.board.board[0][x // square_size] == 0:
                        return x // square_size


