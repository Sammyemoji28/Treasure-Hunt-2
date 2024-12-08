
import pygame
import random
import time
import sys

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Treasure Hunt")

WIDTH = 600
HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (135,206,235)
GREEN = (103,146,103)
RED = (187,17,68)

FPS = 30
clock = pygame.time.Clock()

gridSize = 20
cellSize = WIDTH//gridSize
obstacleNum = 25
score = 0
gameover = False

treasurePos = []
obstaclePos = []
playerPos = [gridSize//2, gridSize//2]

font = pygame.font.SysFont("calibri", 30)

def drawGrid():
    for x in range(0, WIDTH, cellSize): # - 3 parameters : starting #, ending #, size
        pygame.draw.line(screen, WHITE, (x,0), (x,HEIGHT))
    for y in range(0, HEIGHT,cellSize):
        pygame.draw.line(screen, WHITE, (0,y), (WIDTH, y))

def makePlayer():
    pygame.draw.rect(screen, BLUE, (playerPos[0] * cellSize, playerPos[1] * cellSize, cellSize, cellSize))

def makeTreasure():
    for pos in treasurePos:
        pygame.draw.rect(screen, GREEN, (pos[0] * cellSize, pos[1] * cellSize, cellSize, cellSize))

def makeObstacles():
    for pos in obstaclePos:
        pygame.draw.rect(screen, RED, (pos[0] * cellSize, pos[1] * cellSize, cellSize, cellSize))

def resetGame():
    global playerPos, treasurePos, obstaclePos, score
    playerPos = [gridSize//2, gridSize//2]
    treasurePos = [[random.randint(0, gridSize - 1), random.randint(0, gridSize - 1)] for i in range(3)]
    obstaclePos = []
    while len(obstaclePos) < obstacleNum:
        pos = [random.randint(0, gridSize - 1), random.randint(0, gridSize - 1)]
        if pos != playerPos and pos not in treasurePos and pos not in obstaclePos:
            obstaclePos.append(pos)

def checkCollision():
    for pos in treasurePos:
        if pos == playerPos:
            treasurePos.remove(pos)
            return True
    return False

resetGame()

while True:

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and playerPos[0] > 0:
        playerPos[0] -= 1
    if keys[pygame.K_d] and playerPos[0] < gridSize - 1:
        playerPos[0] += 1
    if keys[pygame.K_w] and playerPos[1] > 0:
        playerPos[1] -= 1
    if keys[pygame.K_s] and playerPos[1] < gridSize - 1:
        playerPos[1] += 1

    if playerPos in obstaclePos:
        gameover = True
        score = 0
        resetGame()

    if checkCollision():
        score += 1
        if len(treasurePos) == 0:
            resetGame()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    drawGrid()
    makePlayer()
    makeTreasure()
    makeObstacles()
    text = font.render(f"Score : {str(score)}", False, BLUE)
    screen.blit(text, (30,30))
    clock.tick(FPS)
    pygame.display.flip()