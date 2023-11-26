
import pygame
from pygame.sprite import Sprite



class Ship(Sprite):

    def __init__(self, ai_settings, screen):

        """Initialize the ship and set its starting position."""

        super(Ship, self).__init__()
        
        self.screen = screen



        # Load the ship image and get its rect.

        self.image = pygame.image.load('images/spaceship.bmp') #RJ on X: "Here's a close-up of a spaceship #sprite by @Spudonkey! #gamedev #pixelart http://t.co/fNgIk3bIjL"

        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()
        
        self.ai_settings = ai_settings
        
        self.moving_right = False
        
        self.moving_left = False
        
        self.speed_factor = 1.5
        
        self.center = float(self.rect.centerx)
        
        
        



        # Start each new ship at the bottom center of the screen.

        self.rect.centerx = self.screen_rect.centerx

        self.rect.bottom = self.screen_rect.bottom

    def center_ship(self):
        self.center = self.screen_rect.centerx
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center


    def blitme(self):

        """Draw the ship at its current location."""

        self.screen.blit(self.image, self.rect)
        
    
            