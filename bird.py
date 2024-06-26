import pygame
import random

from pygame import Vector2
from settings import *


class Bird(pygame.sprite.Sprite):
    def __init__(self, game, pos=BIRD_START_POS):
        super().__init__()
        self.game = game
        self.pos = pos
        self.velY = 0
        self.size = BIRD_SIZE
        self.tex = TEXTURES[random.randint(0, len(TEXTURES) - 1)].convert_alpha()
        self.tex = pygame.transform.scale(self.tex, (BIRD_SIZE.x * 1.25, BIRD_SIZE.y * 1.25))
        self.image = pygame.Surface(self.size)
        self.image.fill((220 + random.randint(-30, 30),220 + random.randint(-30, 30), random.randint(0, 5)))
        self.rect = self.image.get_rect(center=self.pos)
        self.Input1 = 0
        self.Input2 = 0
        self.Weight1 = random.uniform(-0.5, 0.5)
        self.Weight2 = random.uniform(-0.5, 0.5)
        self.Bias = random.uniform(-0.5, 0.5)
        self.Output = 0

    def update(self):
        if NEURAL_NETWORK:
            self.Neural_Network()
        self.physics()
        self.blit()
        self.rect.center = self.pos
        if self.pos.y < 0 or self.pos.y > HEIGHT:
            self.death()

    def blit(self):
        self.game.screen.blit(self.tex, self.rect)

    def physics(self):
        self.velY = pygame.math.lerp(self.velY, 7.5, 0.05)
        self.pos.y += self.velY

    def jump(self):
        self.velY = -10

    def death(self):
        if len(self.game.bird.sprites()) <= 1:
            self.game.clean_obstacles()
            change_weight1 = random.uniform(-0.1, 0.1)
            change_weight2 = random.uniform(-0.1, 0.1)
            change_bias = random.uniform(-0.1, 0.1)
            bird1 = Bird(self.game,Vector2(WIDTH/2, HEIGHT/2))
            bird1.Weight1 = self.Weight1 + change_weight1
            bird1.Weight2 = self.Weight2 + change_weight2
            bird1.bias = self.Bias + change_bias

            bird2 = Bird(self.game,Vector2(WIDTH/2, HEIGHT/2))
            bird2.Weight1 = (self.Weight1 - change_weight1)
            bird2.Weight2 = self.Weight2 - change_weight2
            bird2.bias = self.Bias - change_bias

            bird3 = Bird(self.game, Vector2(WIDTH / 2, HEIGHT / 2))
            bird3.Weight1 = self.Weight1
            bird3.Weight2 = self.Weight2
            bird3.bias = self.Bias
            self.game.bird.remove(self)
            self.game.bird.add(bird1)
            self.game.bird.add(bird2)
            self.game.bird.add(bird3)
            self.game.spawn_birds()
        else:
            self.game.bird.remove(self)

    def Neural_Network(self):
        if len(self.game.pillars) > 0:
            vec = self.game.pillars[self.game.current_pillar].pos - self.pos
        else:
            vec = BIRD_START_POS - self.pos
        self.Input1 = vec.y + PILLAR_GAP/2
        self.Input2 = vec.y - PILLAR_GAP/2

        self.Output = (self.Input1 * self.Weight1) + (self.Input2 * self.Weight2) + self.Bias

        if self.Output > 0:
            self.jump()

