import pygame
from .constants import ROWS, COLS, SQUARE_SIZE, BLACK, BOARD_CLR1, BOARD_CLR2


class Board:
    def __init__(self, surface):
        self.board = []
        self.surface = surface

    def draw_board(self):
        self.surface.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(self.surface, BOARD_CLR1, (col * SQUARE_SIZE, row * SQUARE_SIZE,
                                                            SQUARE_SIZE, SQUARE_SIZE))
            for col in range((row + 1) % 2, COLS, 2):
                pygame.draw.rect(self.surface, BOARD_CLR2, (col * SQUARE_SIZE, row * SQUARE_SIZE,
                                                            SQUARE_SIZE, SQUARE_SIZE))

    def update(self):
        self.draw_board()
        pygame.display.update()
