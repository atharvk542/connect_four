import random
import sys
import pygame
from minimaxChooser import MinimaxChooser
from humanChooser import HumanChooser
from connectFourBoard import ConnectFourBoard

class ConnectFour:
    board_size = 8
    board = []
    gameOver = False
    player = 1
    last_move = None
    screen = pygame.display.set_mode((600, 600))

    def __init__(self, board_size):
        self.board = ConnectFourBoard(board_size)
        self.last_move = None
        self.board.drawBoard(pygame, self.screen, self.screen.get_width() // self.board.board_size)
        pygame.display.flip()

    def placePiece(self, col):
        self.board.placePiece(self.player, col, self.screen, pygame)
        self.last_move = col
        self.player = 2 if self.player == 1 else 1

    def simulatePlacePiece(self, col):
        for i in range(self.board.board_size - 1, -1, -1): # iterate backwards from board_size - 1
            if self.board.board[i][col] == 0:
                self.board.board[i][col] = self.player
                self.last_move = self.player
                return self.board
        
        return self.board

    # TODO: create a checkConsecutive that will check for N consecutive in a row
    # which can be used in the minimax evaluateBoard function as well

    # TODO fix the diagonal and anti-diagonal logic
    def checkWin(self):
        # rows
        for i in range(self.board.board_size):
            rowCounter = 1 
            for j in range(1, self.board.board_size):
                if self.board.board[i][j - 1] == self.board.board[i][j] and self.board.	board[i][j] != 0:
                        rowCounter+=1
                else:
                    rowCounter = 1

                if rowCounter >= 4:
                    return True	
        
        # cols
        for i in range(self.board.board_size):
            colCounter = 1
            for j in range(1, self.board.board_size):
                if self.board.board[j - 1][i] == self.board.board[j][i] and self.board.board[j][i] != 0:
                    colCounter+=1
                else:
                    colCounter = 1

                if colCounter >= 4:
                    return True	

        # diagonal
        for i in range(self.board.board_size - 3):
            for j in range(self.board.board_size - 3):
                if (self.board.board[i][j] != 0 and
                    self.board.board[i][j] == self.board.board[i + 1][j + 1] == self.board.board[i + 2][j + 2] == self.board.board[i + 3][j + 3]):
                    return True

        # anti-diagonal
        for i in range(3, self.board.board_size):
            for j in range(self.board.board_size - 3):
                if (self.board.board[i][j] != 0 and
                    self.board.board[i][j] == self.board.board[i - 1][j + 1] == self.board.board[i - 2][j + 2] == self.board.board[i - 3][j + 3]):
                    return True

        return False

    def checkTie(self):
        if not self.checkWin():
            for i in self.board.board:
                for j in i:
                    if j == 0:
                        return False
            
            return True
        
        return False

    def printBoard(self):
        print('-'*10 + "CURRENT BOARD" + '-'*10)
        for i in range(self.board.board_size):
            for j in range(self.board.board_size):
                print(self.board.board[i][j], end=' ')

            print()
        print('-'*33)

if __name__ == "__main__":
    engine = ConnectFour(8)

    running = True
    player_choosers = [HumanChooser(), HumanChooser()]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not running:
            break

        current_chooser = player_choosers[engine.player - 1]
        pygame.display.flip()

        print("player " + str(engine.player) + "'s turn")
        selected_col = current_chooser.choose_move(engine) # TODO: check for valid column choice

        engine.placePiece(selected_col)
        engine.printBoard()

        # TODO: consolidate this into a checkBoard function checking for win and tie
        win = engine.checkWin()
        tie = engine.checkTie()

        if win:
            winner = 2 if engine.player == 1 else 1 # have to flip since engine is already on next move
            print("player " + str(winner) + " has won")
            pygame.time.wait(1000)
            running = False

        if tie:
            print("the game has tied")
            pygame.time.wait(1000)
            running = False

    pygame.quit()
    sys.exit()
        


        
