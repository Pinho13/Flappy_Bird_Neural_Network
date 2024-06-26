import random
import pygame

from pygame import Vector2

RES = (WIDTH, HEIGHT) = (500, 500)
FPS = 60

BACKGROUND_COLOR = (50, 200, 255)
PILLAR_COLOR = (0, 175, 0)
BIRD_COLOR = (220, 220, 0)


BIRD_SIZE = Vector2(20, 20)
BIRD_START_POS = Vector2(WIDTH/2, HEIGHT/2)
PILLAR_SIZE = Vector2(30, HEIGHT)
PILLAR_GAP = 55

TIME_BETWEEN_SPAWNS = 2.5

NUMBER_OF_BIRDS = 10000

NEURAL_NETWORK = True


SCORE_POS = Vector2(WIDTH/2, 25)
TIME_POS = Vector2(WIDTH-125, 25)
GEN_POS = Vector2(50, 25)

TEXTURES = [pygame.image.load("Sprite-0001.png"), pygame.image.load("Sprite-0002.png"), pygame.image.load("Sprite-0003.png"), pygame.image.load("Sprite-0004.png")]
