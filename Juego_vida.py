
import pygame
import numpy as np

ANCHO, ALTO = 800, 600
TAM_CELDA = 10

NEGRO = (0, 0, 0)
BLANCO = (225, 255, 255)

pygame.init()

screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Vida")
reloj = pygame.time.Clock()

rows = ALTO // TAM_CELDA
cols = ANCHO // TAM_CELDA

board = np.zeros((rows, cols), dtype=int)


def actualizarBoard(board):
    new_board = board.copy()

    for row in range(rows):
        for col in range(cols):

            fila_inicio = max(0, row - 1)
            fila_fin = min(rows, row + 2)
            col_inicio = max(0, col - 1)
            col_fin = min(cols, col + 2)

            vecinos = np.sum(
                board[fila_inicio:fila_fin, col_inicio:col_fin]
            ) - board[row, col]

            if board[row, col] == 1 and (vecinos < 2 or vecinos > 3):
                new_board[row, col] = 0

            elif board[row, col] == 0 and vecinos == 3:
                new_board[row, col] = 1

    return new_board


def dibujarBoard(screen, board):
    screen.fill(NEGRO)

    for row in range(rows):
        for col in range(cols):

            if board[row, col] == 1:
                pygame.draw.rect(
                    screen,
                    BLANCO,
                    (
                        col * TAM_CELDA,
                        row * TAM_CELDA,
                        TAM_CELDA - 1,
                        TAM_CELDA - 1
                    )
                )


def cambioCelda(board, x, y):
    col = x // TAM_CELDA
    row = y // TAM_CELDA

    if 0 <= row < rows and 0 <= col < cols:
        board[row, col] = 1 - board[row, col]


corriendo = True
pause = True

while corriendo:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            corriendo = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                pause = not pause

            elif event.key == pygame.K_r:
                board = np.random.choice(
                    [0, 1],
                    size=(rows, cols),
                    p=[0.8, 0.2]
                )

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            cambioCelda(board, x, y)

    if not pause:
        board = actualizarBoard(board)

    dibujarBoard(screen, board)

    pygame.display.flip()
    reloj.tick(10)

pygame.quit()
