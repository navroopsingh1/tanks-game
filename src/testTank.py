import random
import pytest
import Tank
import pygame
import os

#Testing the tank
class TestTank():

    #Intializing the tank
    def setup_method(self):

        self.image = "tankpic.png"

        self.tank = Tank.Tank(self.image, 400, 400, 1, 1)
 
    #Testing if the tank has the ability to move to the right
    def test_move_right(self):

        self.tank.move_right()

        assert(self.tank.location_x == 410)
        
    #Testing if the tank has the ability to move to the left
    def test_move_left(self):
    	
        self.tank.move_left()

        assert(self.tank.location_x == 390)

    #Testing if the tank collides with another tank
    def test_tank_collision(self):

        tank2 = Tank.Tank(self.image, 400, 400, 0, 1)

        assert(self.tank.collide(tank2))

    #Testing if it is the tank's turn to shoot
    def test_tank_is_turn(self):

        assert(self.tank.is_turn())

    #Testing if the tank's power increases
    def test_power_up(self):

        self.tank.power_up()

        assert(self.tank.power == 51)

    #Testing if the tank's power decreases
    def test_power_down(self):

        self.tank.power_down()

        assert(self.tank.power == 49)

    #Testing if the tank shoots
    def test_shoot(self):

        tank2 = Tank.Tank(self.image, 400, 400, 0, 2)

        self.tank.shoot(tank2, 10, 20, 20)

    #Testing if the tank has the ability to move the tank head up
    def test_move_up(self):

        self.tank.move_up()

        assert(self.tank.tank_pos == 1)


    #Testing if the tank has the ability to move the tank head down
    def test_move_down(self):

        self.tank.move_up()

        self.tank.move_down()

        assert(self.tank.tank_pos == 0)

    #Testing if the tank has the ability to move the tank head all the way up
    def test_max_move_up(self):

        for i in range(9):
            self.tank.move_up()

        assert(self.tank.tank_pos == 8)


    #Testing if the tank has the ability to move the tank head all the way down
    def test_max_move_down(self):

        self.tank.move_down()

        assert(self.tank.tank_pos == 0)











 


    

    

  



    



