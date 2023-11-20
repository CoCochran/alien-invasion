import sys
import pygame
from settings import Settings
from ship import Ship
import gamefunctions as gf
from alien import Alien
from pygame.sprite import Group




def run_game():

    # Initialize game and create a screen object
    
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")


    ship = Ship(ai_settings, screen)
    bullets = Group()

    aliens = Group()
    
    
    
    gf.createFleet(ai_settings, screen, ship, aliens)
    
    
    # Start the main loop for the game
    
    while True:

        # Watch for keyboard and mouse events
        gf.checkEvents(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.updateBullets(bullets)
        gf.updateAliens(aliens)
        gf.updateScreen(ai_settings, screen, ship, aliens, bullets)
        


run_game()