import pygame
from .constants import SQUARE_SIZE, WHITE
from .constants import WHITE_PIECES, BLACK_PIECES


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.image = pygame.transform.scale(pygame.image.load("assets/white_king.png"), (44, 44))  # Default sprite

        self.x = 0
        self.y = 0
        self.calc_position()

    def calc_position(self):
        self.x = self.col * SQUARE_SIZE
        self.y = self.row * SQUARE_SIZE

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_position()

    def draw(self, surface):
        surface.blit(self.image, (self.x + self.image.get_width() // 2, self.y + self.image.get_height() // 2))


class Pawn(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.image = WHITE_PIECES["pawn"] if self.color == WHITE else BLACK_PIECES["pawn"]


class Knight(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.image = WHITE_PIECES["knight"] if self.color == WHITE else BLACK_PIECES["knight"]


class Bishop(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.image = WHITE_PIECES["bishop"] if self.color == WHITE else BLACK_PIECES["bishop"]


class Rook(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.image = WHITE_PIECES["rook"] if self.color == WHITE else BLACK_PIECES["rook"]


class Queen(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.image = WHITE_PIECES["queen"] if self.color == WHITE else BLACK_PIECES["queen"]


class King(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.image = WHITE_PIECES["king"] if self.color == WHITE else BLACK_PIECES["king"]
