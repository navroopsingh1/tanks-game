import random
import pytest
import Barrier
import pygame
import os
import Tank

#Testing the barrier
class TestBarrier():

    #Initialzing the barrier object
    def setup_method(self):
        self.barrier = Barrier.Barrier(400, 400)

    #Testing the x of the barrier
    def test_location_x(self):
        assert(self.barrier.location_x == 400)

    #Testing the y location of the barrier
    def test_location_y(self):
        assert(self.barrier.location_y == 400)

    #Testing the width of the barrier
    def test_width(self):
        assert(self.barrier.width == 75)

    #Testing the height of the barrier
    def test_height(self):
        assert(self.barrier.height == 215)

    #Testing to see if the tank is colliding with the tank
    def test_collide_true(self):
        tank = Tank.Tank("tankpic.png", 400, 540, 1, 1)
        assert(self.barrier.collide(tank) == True)

    #Testing to see if the tank is not colliding with the tank
    def test_collide_False(self):
        tank = Tank.Tank("tankpic.png", 300, 400, 1, 1)
        assert(self.barrier.collide(tank) == False)
