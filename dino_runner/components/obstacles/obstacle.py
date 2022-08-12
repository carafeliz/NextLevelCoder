from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from pygame.sprite import Sprite

class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect() #rect devuelve la pantalla y para usarlo se importa pygame
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw (self, screen):
        screen.blit(self.image[self.type], self.rect)