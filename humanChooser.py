import pygame

class HumanChooser:
    def choose_move(self, engine):
        square_size = engine.screen.get_width() // engine.board.board_size

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, _ = pygame.mouse.get_pos()
                    return x // square_size