import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((1250, 600))

pygame.display.set_caption("Dino Jump")
icon = pygame.image.load("D:\Dinosaur Jump\Images\dino.png")
pygame.display.set_icon(icon)

object_1 = pygame.image.load("D:\Dinosaur Jump\Images\sun.png")
object_1X = 480
object_1Y = 50

player = pygame.image.load("D:\Dinosaur Jump\Images\Velociraptor.png")
playerX = 50
playerY = 480
playerX_change = 0.2

enemy1 = (pygame.image.load("D:\Dinosaur Jump\Images\dinosaur-egg.png"))
enemy1X = (random.randint(200, 450))
enemy1Y = 480
enemy1X_change = 0.2    

enemy2 = (pygame.image.load("D:\Dinosaur Jump\Images\dinosaur-egg (1).png"))
enemy2X = (random.randint(550, 800))
enemy2Y = 480
enemy2X_change = 0.2

enemy3 = (pygame.image.load("D:\Dinosaur Jump\Images\stegosaurus (1).png"))
enemy3X = (random.randint(900, 1186))
enemy3Y = 480
enemy3X_change = 0.2

game = pygame.font.Font('freesansbold.ttf', 90)
game_overX = 20
game_overY = 20

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
fontX = 10
fontY = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def object1(x, y):
    screen.blit(object_1, (x, y))

def Player(x, y):
    screen.blit(player, (x, y))

def Enemy1(x, y):
    screen.blit(enemy1, (x, y))

def Enemy2(x, y):
    screen.blit(enemy2, (x, y))

def Enemy3(x, y):
    screen.blit(enemy3, (x, y))

def game_over():
    over_text = game.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (325, 250))

def didCollide_1(playerX, playerY, enemy1X, enemy1Y):
    distance1 = math.sqrt((math.pow(playerX - enemy1X, 2)) + (math.pow(playerY - enemy1Y, 2)))
    if distance1 < 27:
        return True 
    else:
        return False
    
def didCollide_2(playerX, playerY, enemy2X, enemy2Y):
    distance2 = math.sqrt((math.pow(playerX - enemy2X, 2)) + (math.pow(playerY - enemy2Y, 2)))
    if distance2 < 27:
        return True 
    else:
        return False
    
def didCollide_3(playerX, playerY, enemy3X, enemy3Y):
    distance3 = math.sqrt((math.pow(playerX - enemy3X, 2)) + (math.pow(playerY - enemy3Y, 2)))
    if distance3 < 27:
        return True 
    else:
        return False

def jump_key():
    global playerY 
    playerY = 480
    global playerY_change
    playerY_change = 100
    if (playerY == 480):
        playerY -= playerY_change
    if (playerY == 380):
        playerY += 0 

def jump_release():
    global playerY 
    playerY = 480
    global playerY_change
    playerY_change = 100
    if (playerY == 380):
        playerY += playerY_change
    if (playerY == 480):
        playerY += 0 


running = True
while running:
    screen.fill((119, 203, 224))

    playerX += playerX_change

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump_key()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                jump_release()

    playerX += playerX_change
    if playerX >= 1186:
        playerX = 0 
        enemy1X = random.randint(200, 400)
        enemy2X = random.randint(550, 700)
        enemy3X = random.randint(900, 1186)

    if playerX_change > 0:
        score_value += 1

    enemy1X -= enemy1X_change
    enemy2X -= enemy2X_change
    enemy3X -= enemy3X_change

    collision_1 = didCollide_1(playerX, playerY, enemy1X, enemy1Y)
    if collision_1:
        enemy1X_change = 0
        enemy2X_change = 0
        enemy3X_change = 0
        playerX_change = 0 
        playerY_change = 0
        game_over()

    collision_2 = didCollide_2(playerX, playerY, enemy2X, enemy2Y)
    if collision_2:
        enemy1X_change = 0
        enemy2X_change = 0
        enemy3X_change = 0
        playerX_change = 0 
        playerY_change = 0
        game_over()

    collision_3 = didCollide_3(playerX, playerY, enemy3X, enemy3Y)
    if collision_3:
        enemy1X_change = 0
        enemy2X_change = 0
        enemy3X_change = 0
        playerX_change = 0 
        playerY_change = 0
        game_over()
    
    object1(object_1X, object_1Y)
    show_score(fontX, fontY)
    Player(playerX, playerY)
    Enemy1(enemy1X, enemy1Y)
    Enemy2(enemy2X, enemy2Y)
    Enemy3(enemy3X, enemy3Y)

    pygame.display.update()