from turtle import width
import pygame

from dino_runner.components.dinosaur import Dinosaur 
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DEFAULT_TYPE
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
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.high_score = 0
        self.death_count = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()   

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.obstacle_manager.update(self)
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.update_score()
        self.power_up_manager.update(self)

    def update_score(self):
        if self.score == self.high_score:
            self.high_score += 1
            self.score += 1
        elif self.score > self.high_score:
            self.high_score = self.score
        elif self.score < self.high_score:
            self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 2
        
        self.draw_score()
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #Também aceita código hexadecimal "#FFFFFF"
        self.draw_background()
        self.obstacle_manager.draw(self.screen)
        self.player.draw(self.screen)
        self.draw_power_up_time()
        self.draw_score()
        self.power_up_manager.draw(self.screen)
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

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        self.format_text(f"Score: {self.score}", 1000, 80, font)
        self.format_text(f"HighScore: {self.high_score}", 1000, 50, font)
        
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 18)
                self.format_text(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds.", 500, 40, font)
            else:
                self.player.has_power_up = False
                self.player.shield = False
                self.player.hammer = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.death_count > 0:
                    self.score = 0
                    self.game_speed = 20
                self.run()
    

    def format_text(self, text, width, height, font):
        text_formated = font.render(f"{text}", True, (0, 0, 0))
        text_rect = text_formated.get_rect()
        text_rect.center = (width, height)
        self.screen.blit(text_formated, text_rect)

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        font = pygame.font.Font(FONT_STYLE, 22)
        if self.death_count == 0:
            self.format_text("Press any key to start", half_screen_width, half_screen_height, font)
 
        else:
            self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))
            self.format_text("Press any key to restart", half_screen_width, half_screen_height, font)
            self.format_text(f"HighScore: {self.high_score - 1}", half_screen_width, half_screen_height + 30, font)
            self.format_text(f"Score: {self.score - 1}", half_screen_width, half_screen_height + 60, font)
            self.format_text(f"Deaths: {self.death_count}", 100, 50, font)
                                  
        pygame.display.update()
        self.handle_events_on_menu()
        