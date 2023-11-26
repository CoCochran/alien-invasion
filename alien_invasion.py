import sys
import pygame
from settings import Settings
from ship import Ship
import gamefunctions as gf
from alien import Alien
from game_stats import GameStats
from pygame.sprite import Group




def run_game():

    # Initialize game and create a screen object
    
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))   
    pygame.display.set_caption("Alien Invasion")
    

    stats = GameStats(ai_settings)

    alien = Alien(ai_settings, screen)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)
    

    
    
    # Start the main loop for the game
    
    while True:
        gf.checkEvents(ai_settings, screen, ship, bullets)

        # Watch for keyboard and mouse events
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)
            


run_game()