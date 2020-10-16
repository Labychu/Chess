import pygame

WIDTH, HEIGHT = 700, 700
ROWS, COLS = 8, 8
SQUARE_SIZE = HEIGHT // ROWS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOARD_CLR2 = (34, 125, 58)
BOARD_CLR1 = (198, 207, 134)


WHITE_PIECES = {
    "pawn": pygame.transform.scale(pygame.image.load("assets/white_pawn.png"), (44, 44)),
    "knight": pygame.transform.scale(pygame.image.load("assets/white_knight.png"), (44, 44)),
    "bishop": pygame.transform.scale(pygame.image.load("assets/white_bishop.png"), (44, 44)),
    "rook": pygame.transform.scale(pygame.image.load("assets/white_rook.png"), (44, 44)),
    "queen": pygame.transform.scale(pygame.image.load("assets/white_queen.png"), (44, 44)),
    "king": pygame.transform.scale(pygame.image.load("assets/white_king.png"), (44, 44))
}

BLACK_PIECES = {
    "pawn": pygame.transform.scale(pygame.image.load("assets/black_pawn.png"), (44, 44)),
    "knight": pygame.transform.scale(pygame.image.load("assets/black_knight.png"), (44, 44)),
    "bishop": pygame.transform.scale(pygame.image.load("assets/black_bishop.png"), (44, 44)),
    "rook": pygame.transform.scale(pygame.image.load("assets/black_rook.png"), (44, 44)),
    "queen": pygame.transform.scale(pygame.image.load("assets/black_queen.png"), (44, 44)),
    "king": pygame.transform.scale(pygame.image.load("assets/black_king.png"), (44, 44))
}

