import pygame
import os
import Config as cfg
import time
import Physics
import random

#Class for creating the tank
class Tank(pygame.sprite.Sprite):

    #Declare the health for each tank
    health = 200

    #Constructor for the Tank Function
    def __init__(self, image, x, y, turn, id):
        pygame.sprite.Sprite.__init__(self)
        self.location_x = x 
        self.location_y = y
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("Images", image)), (130, 80))
        self.rect = self.image.get_rect()
        self.turn = turn
        self.id = id  
        self.tank_pos = 0
        self.width = 65
        self.power = 50
        self.wind = Physics.wind()
        self.tank_positions1 = [(self.location_x + 27, self.location_y - 2),
                        (self.location_x + 26, self.location_y - 5),
                        (self.location_x + 25, self.location_y - 8),
                        (self.location_x + 23, self.location_y - 12),
                        (self.location_x + 20, self.location_y - 14),
                        (self.location_x + 18, self.location_y - 15),
                        (self.location_x + 15, self.location_y - 17),
                        (self.location_x + 13, self.location_y - 19),
                        (self.location_x + 11, self.location_y - 21)
                        ]

        self.tank_positions2 = [(self.location_x - 27, self.location_y - 2),
                        (self.location_x - 26, self.location_y - 5),
                        (self.location_x - 25, self.location_y - 8),
                        (self.location_x - 23, self.location_y - 12),
                        (self.location_x - 20, self.location_y - 14),
                        (self.location_x - 18, self.location_y - 15),
                        (self.location_x - 15, self.location_y - 17),
                        (self.location_x - 13, self.location_y - 19),
                        (self.location_x - 11, self.location_y - 21)
                        ]

    #Getting the mask used for hit and collision detection for the tank
    def get_mask(self):
        return pygame.mask.from_surface(self.image)

    #Drawing the tank on the game display
    def draw(self):
        return cfg.game_display.blit(self.image, (self.location_x, self.location_y))

    #Defining collision mechanics for the tank
    def collide(self, Tank):
        tank_mask = Tank.get_mask()
        local_tank_mask = pygame.mask.from_surface(self.image)
        offset = (self.location_x - Tank.location_x, self.location_y - Tank.location_y)
        collision_point = tank_mask.overlap(local_tank_mask, offset)

        if collision_point:
            return True

        return False

    #Allowing the tank to move left
    def move_left(self):
        self.location_x -= 10

        self.tank_positions1 = [(self.location_x + 27, self.location_y - 2),
                        (self.location_x + 26, self.location_y - 5),
                        (self.location_x + 25, self.location_y - 8),
                        (self.location_x + 23, self.location_y - 12),
                        (self.location_x + 20, self.location_y - 14),
                        (self.location_x + 18, self.location_y - 15),
                        (self.location_x + 15, self.location_y - 17),
                        (self.location_x + 13, self.location_y - 19),
                        (self.location_x + 11, self.location_y - 21)
                        ]

        self.tank_positions2 = [(self.location_x - 27, self.location_y - 2),
                        (self.location_x - 26, self.location_y - 5),
                        (self.location_x - 25, self.location_y - 8),
                        (self.location_x - 23, self.location_y - 12),
                        (self.location_x - 20, self.location_y - 14),
                        (self.location_x - 18, self.location_y - 15),
                        (self.location_x - 15, self.location_y - 17),
                        (self.location_x - 13, self.location_y - 19),
                        (self.location_x - 11, self.location_y - 21)
                        ]

    #Allowing the tank to move right
    def move_right(self):
        self.location_x += 10

        self.tank_positions1 = [(self.location_x + 27, self.location_y - 2),
                        (self.location_x + 26, self.location_y - 5),
                        (self.location_x + 25, self.location_y - 8),
                        (self.location_x + 23, self.location_y - 12),
                        (self.location_x + 20, self.location_y - 14),
                        (self.location_x + 18, self.location_y - 15),
                        (self.location_x + 15, self.location_y - 17),
                        (self.location_x + 13, self.location_y - 19),
                        (self.location_x + 11, self.location_y - 21)
                        ]

        self.tank_positions2 = [(self.location_x - 27, self.location_y - 2),
                        (self.location_x - 26, self.location_y - 5),
                        (self.location_x - 25, self.location_y - 8),
                        (self.location_x - 23, self.location_y - 12),
                        (self.location_x - 20, self.location_y - 14),
                        (self.location_x - 18, self.location_y - 15),
                        (self.location_x - 15, self.location_y - 17),
                        (self.location_x - 13, self.location_y - 19),
                        (self.location_x - 11, self.location_y - 21)
                        ]
    #Allowing the tank turret to move up
    def move_up(self):

        if self.id == 1:

            self.tank_pos += 1

            if self.tank_pos > 8:
                self.tank_pos = 8

        else:

            self.tank_pos += 1
            if self.tank_pos > 8:
                self.tank_pos = 8


    #Allowing the tank turret to move down
    def move_down(self):

        if self.id == 1:
            self.tank_pos -= 1
            if self.tank_pos < 0:
                self.tank_pos = 0 

        else:

            self.tank_pos -= 1

            if self.tank_pos < 0:
                self.tank_pos = 0 

    #Displaying the current state of the tank
    def is_dead(self):
        if self.health == 0:
            return True

        return False

    #Allowing the tank to shoot
    def shoot(self, tank, barrier, barrier_width, barrier_height):


        if self.id == 1:

            starting_shell = list(self.tank_positions1[self.tank_pos])

            starting_shell[0] += 65
            starting_shell[1] += 10

            fire = True

            while fire:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                pygame.draw.circle(cfg.game_display, cfg.red, (starting_shell[0], starting_shell[1]), 5)

                starting_shell[0] += (12 - self.tank_pos) * 2

                starting_shell[1] += int((((starting_shell[0]  - 100 - self.location_x) * 0.015 / ((self.power - self.wind) / 50)) ** 2) - (self.tank_pos + self.tank_pos / (12 - self.tank_pos)))

                self.wind = Physics.wind()

                if starting_shell[1] > cfg.display_height - cfg.ground_height:


                    hit_x = int((starting_shell[0] * (cfg.display_height - cfg.ground_height))/starting_shell[1])
                    hit_y = int(cfg.display_height - cfg.ground_height)
                    

                    if tank.location_x + tank.width + 15 > hit_x > tank.location_x + tank.width - 15:
                        print("Critical Hit!")
                        tank.health -= 50

                    elif tank.location_x + 20 + tank.width > hit_x > tank.location_x + tank.width - 20:
                        print("Hard Hit!")
                        tank.health -= 36

                    elif tank.location_x + 30 + tank.width > hit_x > tank.location_x - 30 + tank.width:
                        print("Medium Hit")
                        tank.health -= 20

                    elif tank.location_x + 40 + tank.width > hit_x > tank.location_x - 40 + tank.width:
                        print("Light Hit")
                        tank.health -= 10

                    pygame.draw.circle(cfg.game_display, cfg.red, (starting_shell[0], starting_shell[1]), 5)
                    Physics.explosion(hit_x, hit_y)
                    fire = False

                check_x_1 = starting_shell[0] <= barrier + barrier_width
                check_x_2 = starting_shell[0] >= barrier

                check_y_1 = starting_shell[1] <= cfg.display_height
                check_y_2 = starting_shell[1] >= cfg.display_height - barrier_height - cfg.ground_height

                if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                    hit_x = int(starting_shell[0])
                    hit_y = int(starting_shell[1])
                    Physics.explosion(hit_x, hit_y)
                    fire = False 

                pygame.display.update()
                cfg.clock.tick(60)

        else:

            starting_shell = list(self.tank_positions2[self.tank_pos])

            starting_shell[0] += 65
            starting_shell[1] += 10


            fire = True

            while fire:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()


                pygame.draw.circle(cfg.game_display, cfg.red, (starting_shell[0], starting_shell[1]), 5)

                starting_shell[0] -= (12 - self.tank_pos) * 2 

                starting_shell[1] += int((((starting_shell[0] - self.location_x) * 0.015 / ((self.power - self.wind) / 50)) ** 2) - (self.tank_pos + self.tank_pos / (12 - self.tank_pos)))

                self.wind = Physics.wind()

                if starting_shell[1] > cfg.display_height - cfg.ground_height:


                    hit_x =  int((starting_shell[0] * (cfg.display_height - cfg.ground_height))/starting_shell[1])
                    hit_y = int(cfg.display_height - cfg.ground_height)
                    

                    if tank.location_x + 15 + tank.width > hit_x > tank.location_x - 15 + tank.width:
                        print("Critical Hit!")
                        tank.health -= 50

                    elif tank.location_x + 20 + tank.width > hit_x > tank.location_x - 20 + tank.width:
                        print("Hard Hit!")
                        tank.health -= 36

                    elif tank.location_x + 30 + tank.width > hit_x > tank.location_x - 30 + tank.width:
                        print("Medium Hit")
                        tank.health -= 20

                    elif tank.location_x + 40 + tank.width > hit_x > tank.location_x - 40 + tank.width:
                        print("Light Hit")
                        tank.health -= 10

                    Physics.explosion(hit_x, hit_y)
                    fire = False

                check_x_1 = starting_shell[0] <= barrier + barrier_width
                check_x_2 = starting_shell[0] >= barrier

                check_y_1 = starting_shell[1] <= cfg.display_height
                check_y_2 = starting_shell[1] >= cfg.display_height - barrier_height - cfg.ground_height

                if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                    hit_x = int(starting_shell[0])
                    hit_y = int(starting_shell[1])
                    Physics.explosion(hit_x, hit_y)
                    fire = False

                pygame.display.update()
                cfg.clock.tick(60)

    #Displays the tank's current turn
    def is_turn(self):
        if self.turn == 1:
            return True

        return False

    #Increasing the tank's firepower
    def power_up(self):
        self.power += 1

        if self.power >= 100:
            self.power = 100

    #Decreasing the tank's firepower
    def power_down(self):
        self.power -= 1

        if self.power <= 10:
            self.power = 10

    #Drawing the turret onto the game display
    def draw_turret(self):
        if self.id == 1:


            pygame.draw.line(cfg.game_display, cfg.burly, (self.location_x + 65, self.location_y + 10), (self.tank_positions1[self.tank_pos][0] + 65, self.tank_positions1[self.tank_pos][1] + 10), 10)
            


        else:

            pygame.draw.line(cfg.game_display, cfg.burly, (self.location_x + 65, self.location_y + 10), (self.tank_positions2[self.tank_pos][0] +65, self.tank_positions2[self.tank_pos][1] + 10), 10)
            
