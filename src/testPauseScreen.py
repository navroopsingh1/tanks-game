import random
import pytest
import Config
import pygame
import os

#Testing the pause screen
class TestPauseScreen():

	#Testing if the pause screen has the correct width
    def test_pause_screen_width(self):
        assert Config.display_width == 1200

    #Testing if the pause screen has the correct height
    def test_pause_screen_height(self):
        assert Config.display_height == 800

    #Testing if the pause screen has the correct background color
    def test_pause_screen_bg_color(self):
        assert Config.white == (255, 255, 255)

    #Testing if the pause screen screen has the correct font color
    def test_pause_screen_font_color(self):
        assert Config.black == (0, 0, 0)
