import pygame

class Scoreboard:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        
        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font(None, 48)
        
        self.prep_score()
        self.prep_max_score()
        
    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top + 20
        
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)

    def check_max_score(self):
        if self.stats.score > self.stats.max_score:
            self.stats.max_score = self.stats.score
            self.prep_max_score()
            
    def prep_max_score(self):
        rounded_max_score = round(self.stats.max_score, -1)
        max_score_str = "{:,}".format(rounded_max_score)
        self.max_score_image = self.font.render(max_score_str, True, self.text_color, self.settings.bg_color)

        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.centerx = self.screen_rect.centerx
        self.max_score_rect.top = self.score_rect.top