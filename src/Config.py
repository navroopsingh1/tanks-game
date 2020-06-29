import pygame
import sys

#Initializing pygame
pygame.init()

# Window Size
display_width = 1200
display_height = 800

# Height of Ground
ground_height = 125


# Color Definitions
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 255)
yellow = (255,255,0)
navy = (16, 61, 122)
burly = (102, 102, 51)

# Create Game Display
game_display = pygame.display.set_mode((display_width, display_height))

# Set Game Display Caption
pygame.display.set_caption('Tanks')

# Create Game Clock
clock = pygame.time.Clock()

# Font Definitions 
small_font = pygame.font.SysFont("Lato", 35)
med_font = pygame.font.SysFont("Lato", 70)
large_font = pygame.font.SysFont("Lato", 160)


# Method to Create Text Objects
def text_objects(text, color, size):

    if size == "small_font":

        textSurface = small_font.render(text, True, color)

    elif size == "med_font":

        textSurface = med_font.render(text, True, color)

    elif size == "large_font":

        textSurface = large_font.render(text, True, color)

    return textSurface, textSurface.get_rect()

# Method to Send Text Objects to the screen
def message_to_screen(msg, color, y_displace=0, size="small_font"):

    textSurf, textRect = text_objects(msg, color, size)

    textRect.center = (display_width / 2), (display_height / 2) + y_displace

    game_display.blit(textSurf, textRect)

# Method to Pause the Game
def pause():

    paused = True

    while paused:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_c:

                    paused = False

                elif event.key == pygame.K_q:

                    pygame.quit()

                    quit()

        game_display.fill(white)

        message_to_screen("Paused", black, -100, size="large_font")

        message_to_screen("Press C to continue or Q to quit.", black, 25)

        pygame.display.update()

        clock.tick(5)

# Method to Create Buttons
def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small_font"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    game_display.blit(textSurf, textRect)


# Method To Map Buttons to Actions
def button(text, x, y, width, height, inactive_color, active_color, action=None,size=" "):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(game_display, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "play":
                return "Play"

            if action == "controls":
                return "Controls"

            if action == "main":
                return "Main"



    else:
        pygame.draw.rect(game_display, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)

#Method for displaying the health bars of the tank on the game display
def health_bars(tank_1, tank_2):
    if tank_1.health >= 75:
        tank1_color = green

    elif tank_1.health >= 50:
        tank1_color = yellow

    else:
        tank1_color = red


    if tank_2.health >= 75:
        tank2_color = green

    elif tank_2.health >= 50:
        tank2_color = yellow

    else:
        tank2_color = red

    pygame.draw.rect(game_display, tank1_color, (890, 60, tank_1.health, 20))
    pygame.draw.rect(game_display, tank2_color, (50, 60, tank_2.health, 20))

# Method for displaying the power level of the tank
def power(tank):

    if tank.id == 1:

        text = med_font.render("Power: " + str(tank.power) + "%", True, white)
        game_display.blit(text, [display_width / 25, 0])

    else:

        text = med_font.render("Power: " + str(tank.power) + "%", True, white)
        game_display.blit(text, [display_width / 1.35, 0])

#Method for displaying the current turn of each tank
def turn(tank):
    if tank.is_turn() and tank.id == 1:
        text = small_font.render(" Tank 1 Turn ", True, white)
        game_display.blit(text, [display_width/2-50, 20])

    if tank.is_turn() and tank.id == 2:
        text = small_font.render(" Tank 2 Turn", True, white)
        game_display.blit(text, [display_width/2-50  , 20 ])

#Method for displaying the wind affecting each shell
def wind(tank1, tank2):

    if tank1.is_turn():

        if tank1.wind < 0:

            text = med_font.render("Wind: " + str(tank1.wind) + "km/h", True, white)
            game_display.blit(text, [display_width/2-120,50])


        elif tank1.wind > 0:

            text = med_font.render("Wind: " + str(tank1.wind) + "km/h", True, white)
            game_display.blit(text, [display_width/2-120,50])
  

        else:
            text = med_font.render("Wind: " + str(tank1.wind) + "km/h", True, white)
            game_display.blit(text, [display_width/2-120,50])


    if tank2.is_turn():


        if tank2.wind < 0:

            text = med_font.render("Wind: " + str(tank2.wind) + "km/h", True, white)
            game_display.blit(text, [display_width/2-120 ,50])


        elif tank2.wind > 0:

            text = med_font.render("Wind: " + str(tank2.wind) + "km/h", True, white)
            game_display.blit(text, [display_width/2-120 ,50])

        else:
            text = med_font.render("Wind: " + str(tank2.wind) + "km/h", True, white)
            game_display.blit(text, [display_width/2-120 ,50])


















