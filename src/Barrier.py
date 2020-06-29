import pygame
import os
import Config as cfg

#Class for creating the barrier of the game
class Barrier(pygame.sprite.Sprite):

    #Constructor for the barrier
    def __init__(self, location_x, location_y):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("Images", "barrier.png")), (75, 215))
        self.rect = self.image.get_rect()
        self.width = 75
        self.height = 215
        self.location_x = location_x
        self.location_y = location_y  

    #Drawing the barrier onto the game display
    def draw(self):
        return cfg.game_display.blit(self.image, (self.location_x, self.location_y))

    #Acquiring the mask used for collision detection
    def get_mask(self):
        return pygame.mask.from_surface(self.image)

    #Defining the collision between the barrier and the tanks
    def collide(self, tank):
        tank_mask = tank.get_mask()
        barrier_mask = pygame.mask.from_surface(self.image)
        offset = (self.location_x - tank.location_x, self.location_y - tank.location_y + 140)

        collision_point = tank_mask.overlap(barrier_mask, offset)

        if collision_point:
            return True

        return False