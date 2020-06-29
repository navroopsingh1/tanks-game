import pygame
import random
import Config as cfg
import os

# Defining the explosion of the tank shell
def explosion(x, y, size=50):

    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x, y

        print(startPoint)

        cfg.game_display.blit(pygame.transform.scale(pygame.image.load(os.path.join("Images", "explosion.png")), (10, 10)), (x, y))

        pygame.display.update()

        cfg.clock.tick(100)

        explode = False

#Defining the wind affecting each tank shell
def wind():

	wind_factor = random.randint(-5, 5)

	return wind_factor

