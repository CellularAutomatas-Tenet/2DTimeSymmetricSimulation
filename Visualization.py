import pygame

WIDTH = 360
HEIGHT = 480
FPS = 30
screen = 0
clock = 0


def __init__():
    global screen, clock
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Cellular automata")
    clock = pygame.time.Clock()
    screen.fill((100, 150, 100))
    pygame.display.flip()


def draw(field_1, field_2, ca_1, ca_2):
    size = min(WIDTH, HEIGHT)
    cell_size = size / len(field_1)
    screen.fill((100, 150, 100))
    for i in range(len(field_1)):
        for j in range(len(field_1[i])):
            pygame.draw.rect(screen, ca_1.state_to_color(field_1[i][j], True),
                             (i * cell_size, j * cell_size, cell_size, cell_size))
            pygame.draw.circle(screen, ca_2.state_to_color(field_2[i][j], False),
                               ((i + 0.5) * cell_size, (j + 0.5) * cell_size), cell_size / 3)

    pygame.display.flip()