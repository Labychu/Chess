import pygame
from chess.constants import WIDTH, HEIGHT
from chess.board import Board


FPS = 60
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board(WIN)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.update()
    pygame.quit()


if __name__ == '__main__':
    main()
