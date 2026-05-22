import pygame

class ConnectFourBoard:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[0 for _ in range(board_size)] for _ in range(board_size)]
        self.player = 1
        self.gameOver = False
        self.last_move = None

    def placePiece(self, col, screen, pygame):
        j = col
        for i in range(self.board_size - 1, -1, -1): # iterate backwards from board_size - 1
            if self.board[i][j] == 0:
                placed_by = self.player
                self.board[i][j] = self.player
                self.player = 2 if self.player == 1 else 1
                self.last_move = (i, j, placed_by)
                self.drawBoard(pygame, screen, 600 // self.board_size)
                pygame.display.flip()
                return self.board
        
        return self.board
    
    def drawBoard(self, pygame, screen, square_size):
        for i in range(self.board_size):
            for j in range(self.board_size):
                color = (255, 255, 255) if self.board[i][j] == 0 else (255, 0, 0) if self.board[i][j] == 1 else (255, 255, 0)
                pygame.draw.circle(screen, color, (j * square_size + square_size // 2, i * square_size + square_size // 2), square_size // 2 - 5)
                pygame.display.flip()