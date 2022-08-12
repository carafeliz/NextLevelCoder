import random
from pygame.sprite import Sprite
from ..utils.constants import CLOUD, SCREEN_WIDTH

class Cloud(Sprite):
    def __init__ (self):
        self.image = CLOUD
        self.rect = self.image.get_rect() 
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.randint(50, 100)
        self.width = self.image.get_width()
        #self.game_speed = 14

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x < self.width:
            self.rect.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.rect.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))