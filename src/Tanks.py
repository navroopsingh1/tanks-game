import pygame
import Config as cfg
import Tank
import Barrier
import Background
import random
import os
import time
import sys
import Physics


#Preventing the recursion limit of the gameloop to close the game
sys.setrecursionlimit(10000)


Images = ["tankpic2.png", "tankpic.png"]

barrier = Barrier.Barrier(random.randint(450, 600), 470)

tank1 = Tank.Tank(Images[0], 800, 610, 1, 2)

tank2 = Tank.Tank(Images[1], 300, 610, 0, 1)

bg = Background.Background()



# The introduction screen of the game
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        cfg.game_display.fill(cfg.navy)
        cfg.message_to_screen("TANKS", cfg.white, -125, size="large_font")
        cfg.message_to_screen("The objective is to shoot and destroy", cfg.white, 15)
        cfg.message_to_screen("the enemy tank before they destroy you.", cfg.white, 60)
        cfg.message_to_screen("Created by Eric Liang, Amrit Pandher, and Navroop Singh", cfg.white, 280)

        event = cfg.button("Play", 275, 550, 150, 50, cfg.white, cfg.green, action="play",size="small_font")
        if event == "Play":
            game_loop()
        event = cfg.button("Controls", 525, 550, 150, 50, cfg.white, cfg.yellow, action="controls",size="small_font")
        if event == "Controls":
            game_controls()

        event = cfg.button("Quit", 775, 550, 150, 50, cfg.white, cfg.red, action="quit",size="small_font")

        pygame.display.update()

        cfg.clock.tick(15)

# The controls screen of the game
def game_controls():
    gcont = True

    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        cfg.game_display.fill(cfg.navy)
        cfg.message_to_screen("Controls for Player 1", cfg.white, -300, size="med_font")
        cfg.message_to_screen("Fire: Left ALT", cfg.white, -250)
        cfg.message_to_screen("Move Turret: Up and Down arrows", cfg.white, -210)
        cfg.message_to_screen("Move Tank: Left and Right arrows", cfg.white, -170)
        cfg.message_to_screen("Press Left Shift to raise Power % AND Press Left Control to lower Power % ", cfg.white, -130)
        cfg.message_to_screen("Pause: P", cfg.white, -90)

        cfg.message_to_screen("Controls for Player 2", cfg.white, 0, size="med_font")
        cfg.message_to_screen("Fire: Right ALT", cfg.white, 40)
        cfg.message_to_screen("Move Turret: W and S arrows", cfg.white, 80)
        cfg.message_to_screen("Move Tank: A and D", cfg.white, 120)
        cfg.message_to_screen("Press Right Shift to raise Power % AND Press Right Control to lower Power % ", cfg.white, 160)
        cfg.message_to_screen("Pause: P", cfg.white, 200)




        event = cfg.button("Main", 475, 700, 100, 50, cfg.white, cfg.green, action="main")

        if event == "Main":
            game_intro()

        event = cfg.button("Quit", 625, 700, 100, 50, cfg.white, cfg.red, action="quit")

        pygame.display.update()

        cfg.clock.tick(15)

# The game loop with containing the game logic of the game
def game_loop():

    tank1shoot = False

    tank2shoot = False

    game_exit = False

    game_over = False

    FPS = 30

    while not game_exit:

        bg.draw()

        while game_over:

            cfg.message_to_screen("Game over!", cfg.red, y_displace=-50, size="large_font")

            cfg.message_to_screen("Press C to play again or Q to quit", cfg.black, y_displace=50, size="med_font")

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    game_exit = True

                    game_over = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:

                        game_exit = True

                        game_over = False

                    if event.key == pygame.K_c:

                        tank1.health = 200
                        tank2.health = 200
                        tank1.power = 50
                        tank2.power = 50

                        game_loop()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                game_exit = True

            if event.type == pygame.KEYDOWN:

                pass

                if event.key == pygame.K_LEFT and tank1.is_turn():

                    tank1.move_left()

                elif event.key == pygame.K_RIGHT and tank1.is_turn():

                    tank1.move_right()

                elif event.key == pygame.K_UP and tank1.is_turn():

                    tank1.move_up()

                elif event.key == pygame.K_DOWN and tank1.is_turn():

                    tank1.move_down()

                elif event.key == pygame.K_LSHIFT and tank2.is_turn():

                    tank2.power_up()

                elif event.key == pygame.K_LCTRL and tank2.is_turn():

                    tank2.power_down()

                elif event.key == pygame.K_RSHIFT and tank1.is_turn():

                    tank1.power_up()

                elif event.key == pygame.K_RCTRL and tank1.is_turn():

                    tank1.power_down()

                elif event.key == pygame.K_p:

                    cfg.pause()

                elif event.key == pygame.K_w and tank2.is_turn():

                    tank2.move_up()

                elif event.key == pygame.K_a and tank2.is_turn():

                    tank2.move_left()

                elif event.key == pygame.K_s and tank2.is_turn():

                    tank2.move_down()

                elif event.key == pygame.K_d and tank2.is_turn():

                    tank2.move_right()

                elif event.key == pygame.K_RALT and tank1.is_turn():

                    if tank1.is_turn():
                        tank1shoot = True

                elif event.key == pygame.K_LALT and tank2.is_turn():

                    if tank2.is_turn():
                        tank2shoot = True


        tank1.draw()

        tank2.draw()

        barrier.draw()

        cfg.wind(tank2, tank1)


        if tank1shoot and tank1.is_turn():
            tank1.shoot(tank2, barrier.location_x, barrier.width, barrier.height)
            tank1shoot = False
            tank1.turn = 0
            tank2.turn = 1

        elif tank2shoot and tank2.is_turn():
            tank2.shoot(tank1, barrier.location_x, barrier.width, barrier.height)
            tank2shoot = False
            tank2.turn = 0 
            tank1.turn = 1

        cfg.turn(tank1)

        cfg.turn(tank2)


        if tank1.collide(tank2):

            tank1.location_x = tank1.location_x + 10

            tank2.location_x = tank2.location_x - 10

        if (barrier.collide(tank1)): 

            tank1.location_x += 10

        if (barrier.collide(tank2)):

            tank2.location_x -= 10

        if tank1.location_x >= cfg.display_width -120:

            tank1.location_x = cfg.display_width -120

        if tank2.location_x <= 0:

            tank2.location_x = 0


        if tank1.health <= 0 or tank2.health <= 0:

            game_over = True

        cfg.health_bars(tank1, tank2)

        cfg.power(tank1)
        cfg.power(tank2)

        tank1.draw_turret()
        tank2.draw_turret()


        pygame.display.update()

        cfg.clock.tick(FPS)

    pygame.quit()

    quit()


# Start The Intro and The Game Loop
game_intro()
game_loop()
