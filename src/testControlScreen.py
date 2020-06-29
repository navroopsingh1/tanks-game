import random
import pytest
import Config
import pygame
import os


#Testing the controls screen
class TestControlScreen():

    def setup_method(self):
        pass

    #Testing to see if the control screen is visible
    def test_control_screen_visible(self):
        try:
            import Tanks
        except SystemExit:
            assert True
        else:
            assert False

    #Testing to see if the screen has the correct width
    def test_screen_width(self):
        assert Config.display_width == 1200

    #Testing to see if the screen has the correct height
    def test_screen_height(self):
        assert Config.display_height == 800

    #Testing to see if the screens background color is correct
    def test_screen_bg_color(self):
        assert Config.navy == (16, 61, 122)

    def test_controls_screen_main_button(self):
        pass

    def test_controls_screen_quit_button(self):
        pass

    def test_controls_for_player1_text(self):
        pass

    def test_controls_for_player2_text(self):
        pass

