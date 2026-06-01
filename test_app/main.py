import pygame
import random

pygame.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Minecraft Mobile (Thin Bedrock)")
clock = pygame.time.Clock()

GRASS = (34, 139, 34)
DIRT = (139, 69, 19)
STONE = (128, 128, 128)
DEEPSLATE = (64, 64, 64)
ORE = (255, 215, 0)
BEDROCK = (0, 0, 0)
SKY = (135, 206, 235)

BLOCK_SIZE = 40
WORLD_WIDTH = WIDTH // BLOCK_SIZE
WORLD_HEIGHT = HEIGHT // BLOCK_SIZE

world = [[None for _ in range(WORLD_HEIGHT)] for _ in range(WORLD_WIDTH)]

SURFACE_HEIGHT = WORLD_HEIGHT // 4

for x in range(WORLD_WIDTH):
    for y in range(WORLD_HEIGHT):
        if y < SURFACE_HEIGHT:
            world[x][y] = None
        elif y == SURFACE_HEIGHT:
            world[x][y] = GRASS
        elif y < SURFACE_HEIGHT + 3:
            world[x][y] = DIRT
        elif y < SURFACE_HEIGHT + 15:
            if random.random() < 0.1:
                world[x][y] = ORE
            else:
                world[x][y] = STONE
        elif y < WORLD_HEIGHT - 2:
            if random.random() < 0.15:
                world[x][y] = ORE
            else:
                world[x][y] = DEEPSLATE
        else:
            world[x][y] = BEDROCK

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            block_x = mouse_x // BLOCK_SIZE
            block_y = mouse_y // BLOCK_SIZE
            
            if (0 <= block_x < WORLD_WIDTH and 
                0 <= block_y < WORLD_HEIGHT and 
                world[block_x][block_y] != BEDROCK):
                world[block_x][block_y] = None

    screen.fill(SKY)
    for x in range(WORLD_WIDTH):
        for y in range(WORLD_HEIGHT):
            block = world[x][y]
            if block is not None:
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, block, rect)
                pygame.draw.rect(screen, (50, 50, 50), rect, 1)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
