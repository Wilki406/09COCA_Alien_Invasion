class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (255, 255, 255)
        self.bg_background = pygame.image.load("images/1219598.jpg")
        self.bg_background = pygame.transform.scale(self.bg_background, (1366, 768))
        clock = pygame.time.Clock()
        fps = 60

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 9999999

        # Alien settings.
        self.fleet_drop_speed = 10

        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # How quickly the alien point values increase.
        self.score_scale = 3

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 7
        self.bullet_speed_factor = 17
        self.alien_speed_factor = 5

        # Scoring.
        self.alien_points = 50

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        #self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

import pygame
from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load('Fred.mp3')

# Setting the volume
mixer.music.set_volume(0.1)

# Start playing the song
mixer.music.play()
