import random
import pygame
from dino_runner.components.obstacles.small_cactus import SmallCactus
from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS,LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__ (self):
        self.obstacles = []

    def update(self,death_count, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect): #de pygame
                if not game.player.shield:
                    pygame.time.delay(2000)
                    death_count += 1
                    game.playing = False
                    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

        