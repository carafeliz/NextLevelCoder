import pygame, sys
from .cloud import Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 17
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.death_count = 0
        self.player = Dinosaur() #
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.power_up_manager = PowerUpManager()
        self.cloud = Cloud()
        

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def create_componets(self):
        self.power_up_manager.reset_power_up(self.points)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False


    def update(self):
        user_input = pygame.key.get_pressed() 
        self.player.update(user_input)
        self.obstacle_manager.update(self.death_count,self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        self.cloud.update(self.game_speed)

    def draw(self):
        #self.menu()
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.score()
        self.draw_background()
        self.player.draw(self.screen) #
        self.obstacle_manager.draw(self.screen)#
        self.power_up_manager.draw(self.screen)#
        self.cloud.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        self.player.check_invincibility(self.screen)
        font = pygame.font.Font('freesansbold.ttf', 18)
        text = font.render(f'Points: {self.points}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        self.screen.blit(text, text_rect)
        #print(self.points)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.K_DOWN:
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    pygame.quit()
                    sys.exit
                else:
                    self.points = 0
                    self.run()

    def menu(self):
        while self.playing:
            self.screen.fill((255, 255, 255))

            font = pygame.font.Font('freesansbold.ttf', 25)
            if  self.death_count == 0:
                text = font.render("Press a key to start the game", True, (0, 0, 0))
            elif self.death_count > 0:
                text = font.render("Press a key to start the game", True, (0, 0, 0))
                score = font.render("Score: ", {self.points}, True, (0, 0, 0))
                score_rect = score.get_rect()
                score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
                self.screen.blit(score, score_rect)
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            self.screen.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 -140))
            pygame.display.update()
            self.handle_key_events_on_menu()
            
