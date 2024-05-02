import pygame

from random import *
from pygame import Vector2
from settings import *


class Pillars(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.pos = Vector2(WIDTH + 50, randint(100, HEIGHT-100))
        self.Y1 = self.pos.y + (HEIGHT/2) + PILLAR_GAP
        self.Y2 = self.pos.y - (HEIGHT / 2) - PILLAR_GAP
        self.pillar1 = Pillar(Vector2(self.pos.x, self.Y1), game)
        self.pillar2 = Pillar(Vector2(self.pos.x, self.Y2), game)
        self.game.obstacles.add(self.pillar1)
        self.game.obstacles.add(self.pillar2)
        self.point_added = False

    def update(self):
        self.pos.x -= 1
        if self.pos.x < -20:
            self.game.obstacles.remove(self.pillar1)
            self.game.obstacles.remove(self.pillar2)
            self.game.pillars.remove(self)
            self.game.current_pillar -= 1
        if self.pos.x < (WIDTH/2)-30 and not self.point_added:
            self.point_added = True
            self.game.current_pillar += 1
            self.game.score += 1
            self.game.score_text.text = str(self.game.score)


class Pillar(pygame.sprite.Sprite):
    def __init__(self, pos, game):
        super().__init__()
        self.game = game
        self.pos = pos
        self.image = pygame.Surface(PILLAR_SIZE)
        self.image.fill(PILLAR_COLOR)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self):
        self.pos.x -= 1
        self.rect.center = Vector2(self.pos.x, self.pos.y)
