import pygame
import sys

from pygame import Vector2
from settings import *
from bird import *
from Obstacles import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.delta_time = 0
        self.bird = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.pillars = []
        self.has_started = False
        self.clock = pygame.time.Clock()
        self.time_counter = 0
        self.last_spawn = 0
        self.current_pillar = 0
        self.initializer()

    def initializer(self):
        self.spawn_birds()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.has_started = True

                for b in self.bird:
                    if isinstance(b, Bird):
                        b.jump()

    def update(self):
        self.delta_time = self.clock.tick(FPS) / 1000
        self.time_counter += self.delta_time
        pygame.display.set_caption('Flappy Bird - ' + str(round(self.clock.get_fps())))
        self.screen.fill(BACKGROUND_COLOR)
        self.bird.draw(self.screen)
        self.obstacles.draw(self.screen)
        if self.has_started:
            self.bird.update()
            self.obstacles.update()
            self.spawn_pillars()
            for i in self.pillars:
                if isinstance(i, Pillars):
                    i.update()
        if len(self.bird) <= 0:
            self.clean_obstacles()
            self.initializer()
        for bird in self.bird:
            if pygame.sprite.spritecollideany(bird, self.obstacles):
                if isinstance(bird, Bird):
                    bird.death()
        #self.debug()
        pygame.display.update()

    def spawn_pillars(self):
        if self.time_counter - self.last_spawn >= TIME_BETWEEN_SPAWNS:
            self.pillars.append(Pillars(self))
            self.last_spawn = self.time_counter

    def spawn_birds(self):
        if NEURAL_NETWORK:
            for i in range(NUMBER_OF_BIRDS - len(self.bird.sprites())):
                self.bird.add(Bird(self,Vector2(WIDTH/2, HEIGHT/2))) # noqa
        else:
            self.bird.empty()
            self.bird.add(Bird(self, Vector2(WIDTH / 2, HEIGHT / 2)))  # noqa

    def clean_obstacles(self):
        self.current_pillar = 0
        self.obstacles.empty()
        self.pillars.clear()

    def debug(self):
        if len(self.pillars) > 0:
            self.image = pygame.Surface(Vector2(1000, 10))
            self.image.fill(BIRD_COLOR)
            self.rect = self.image.get_rect(center=self.pillars[self.current_pillar].pos)
            self.screen.blit(self.image, self.rect)
            print(self.pillars[self.current_pillar].pos)
            print(self.pillars[self.current_pillar].point_added)

    def run(self):
        while True:
            self.check_events()
            self.update()


if __name__ == "__main__":
    game = Game()
    game.run()
