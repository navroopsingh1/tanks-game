import pygame
import os
import Config as cfg

#Class for creating the background of the game
class Background(pygame.sprite.Sprite):

	#Constructer for the background class
    def __init__(self,):
        self.image= pygame.image.load(os.path.join("Images","bg.png"))
        self.rect = self.image.get_rect()
        self.location_x = 0
        self.location_y = 0

    #Drawing the background onto the game display
    def draw(self):
        return cfg.game_display.blit(self.image, (self.location_x, self.location_y))