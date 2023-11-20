
import pygame



class Ship():

    def __init__(self, ai_settings, screen):

        """Initialize the ship and set its starting position."""

        self.screen = screen



        # Load the ship image and get its rect.

        self.image = pygame.image.load('images/spaceship.bmp') #RJ on X: "Here's a close-up of a spaceship #sprite by @Spudonkey! #gamedev #pixelart http://t.co/fNgIk3bIjL"

        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()
        
        self.ai_settings = ai_settings
        
        self.movingRight = False
        
        self.movingLeft = False
        
        self.speedFactor = 1.5
        
        self.center = float(self.rect.centerx)
        
        
        



        # Start each new ship at the bottom center of the screen.

        self.rect.centerx = self.screen_rect.centerx

        self.rect.bottom = self.screen_rect.bottom

    def update(self):
        if self.movingRight and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.shipSpeedFactor
        if self.movingLeft and self.rect.left > 0:
            self.center -= self.ai_settings.shipSpeedFactor
        self.rect.centerx = self.center


    def blitme(self):

        """Draw the ship at its current location."""

        self.screen.blit(self.image, self.rect)
        
    
            