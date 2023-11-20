import sys
import pygame
from math import floor
from alien import Alien
from bullet import Bullet

        
def updateBullets(bullets):
     for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
                    
def fireBullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
                newBullet = Bullet(ai_settings, screen, ship)
                bullets.add(newBullet)

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) / ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    
    return number_rows

def getAlienNumber(ai_settings, width):
    alien = Alien(ai_settings, width)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_X = available_space_x / (2 * alien_width)
    
    return number_aliens_X

def createAlien(ai_settings, screen, aliens, alienNumber, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = getAlienNumber(ai_settings, alien.rect.width)
    


    alien.x = alien_width + 2 * alien_width * alienNumber
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)
                
def createFleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)

    number_aliens_x = getAlienNumber(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    for row_number in range(number_rows):
        for alienNumber in range(floor(number_aliens_x)):
            createAlien(ai_settings, screen, aliens, alienNumber, row_number)

def updateAliens(aliens):
    aliens.update()
    
        
   

        

    
                
                
def checkKeyDown(ai_settings, screen, ship, bullets):
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #Move the ship to the right
                ship.movingRight = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_LEFT:
                ship.movingLeft = True
            elif event.key == pygame.K_SPACE:
                fireBullet(ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                #Move the ship to the right
                ship.movingRight = False
            elif event.key == pygame.K_LEFT:
                ship.movingLeft = False
        
            
    
def checkEvents(ai_settings, screen, ship, bullets):
    checkKeyDown(ai_settings, screen, ship, bullets)

    

def updateScreen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    aliens.draw(screen)

        # Make the most recently drawn screen visible

    pygame.display.flip()