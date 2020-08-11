import pygame
from random import randint
from copy import deepcopy

RES = WIDTH, HEIGHT = 1500, 900
TILE = 30
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 6

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()



next_field = [[0 for i in range(W)] for j in range(H)]
current_field = [[0 for i in range(W)] for j in range(H)]
current_field = [[1 if i == W // 2 or j == H // 2 else 0 for i in range(W)] for j in range(H)]
# current_field = [[randint(0, 1) for i in range(W)] for j in range(H)]
# current_field = [[1 if not i % 9 else 0 for i in range(W)] for j in range(H)] # 2,5,8,9,10,11,13,18,21,22,26,30,33,65
# current_field = [[1 if not (2 * i + j) % 4 else 0 for i in range(W)] for j in range(H)] # (2,4),(4,4)
# current_field = [[1 if not (i * j) % 22 else 0 for i in range(W)] for j in range(H)] # 5,6,9,22,33
# current_field = [[1 if not i % 7 else randint(0, 1) for i in range(W)] for j in range(H)]

def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


while True:

    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
    # draw life
    for x in range(1, W - 1):
        for y in range(1, H - 1):
            if current_field[y][x]:
                pygame.draw.rect(surface, pygame.Color('forestgreen'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
            next_field[y][x] = check_cell(current_field, x, y)

    current_field = deepcopy(next_field)

    print(clock.get_fps())
    pygame.display.flip()
    clock.tick(FPS)
