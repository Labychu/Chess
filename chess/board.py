import pygame
from .constants import ROWS, COLS, SQUARE_SIZE, BLACK, WHITE, BOARD_CLR1, BOARD_CLR2
from .piece import Pawn, Knight, Bishop, Rook, King, Queen


class Board:
    def __init__(self, surface):
        self.board = []
        self.surface = surface  # surface is the display window

        self.init_board()

    # Display the board onto the surface and only the board
    def draw_board(self):
        self.surface.fill(BLACK)  # bg fill
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(self.surface, BOARD_CLR1, (col * SQUARE_SIZE, row * SQUARE_SIZE,
                                                            SQUARE_SIZE, SQUARE_SIZE))
            for col in range((row + 1) % 2, COLS, 2):
                pygame.draw.rect(self.surface, BOARD_CLR2, (col * SQUARE_SIZE, row * SQUARE_SIZE,
                                                            SQUARE_SIZE, SQUARE_SIZE))

    def init_board(self):
        for row in range(ROWS):
            # add an empty row
            self.board.append([])
            if row == 0:
                self.board[row].append(Rook(0, 0, BLACK))
                self.board[row].append(Knight(0, 1, BLACK))
                self.board[row].append(Bishop(0, 2, BLACK))
                self.board[row].append(Queen(0, 3, BLACK))
                self.board[row].append(King(0, 4, BLACK))
                self.board[row].append(Bishop(0, 5, BLACK))
                self.board[row].append(Knight(0, 6, BLACK))
                self.board[row].append(Rook(0, 7, BLACK))
            elif row == 1:
                for col in range(COLS):
                    self.board[row].append(Pawn(row, col, BLACK))
            elif row == 6:
                for col in range(COLS):
                    self.board[row].append(Pawn(row, col, WHITE))
            elif row == 7:
                self.board[row].append(Rook(7, 0, WHITE))
                self.board[row].append(Knight(7, 1, WHITE))
                self.board[row].append(Bishop(7, 2, WHITE))
                self.board[row].append(Queen(7, 3, WHITE))
                self.board[row].append(King(7, 4, WHITE))
                self.board[row].append(Bishop(7, 5, WHITE))
                self.board[row].append(Knight(7, 6, WHITE))
                self.board[row].append(Rook(7, 7, WHITE))
            else:
                for col in range(COLS):
                    self.board[row].append(0)

    def get_piece(self, row, col):
        return self.board[row][col]

    def update(self):
        self.draw_board()
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.get_piece(row, col)
                if piece != 0:
                    piece.draw(self.surface)
        pygame.display.update()
