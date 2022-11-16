import pygame
from coo import *
pygame.init()

class Game:
    def __init__(self):
        self.player = Player()



class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load('assets/virus.png')
        self.rect = self.image.get_rect()
        self.rect.x = 580
        self.rect.y = 120
        
    def move_right(self):
        self.rect.x += 70
        self.rect.y -= 70
        
    def move_left(self):
        self.rect.x -= 70
        self.rect.y += 70
    
    def move_up(self):
        self.rect.y -= 70
        self.rect.x -= 70
        
    def move_down(self):
        self.rect.y += 70
        self.rect.x += 70
        





pygame.display.set_caption("Antivirus")
screen = pygame.display.set_mode((960,600))

bg = pygame.image.load("assets/download.jpg")

game = Game()

running = True

while running:
    
    screen.blit(bg,(0,0))
    screen.blit(game.player.image, game.player.rect)
    
    pygame.display.flip()
    print(game.player.rect.x , game.player.rect.y)
    for event in pygame.event.get():
        
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("jeux quitté")
            
            
        elif event.type == pygame.KEYDOWN:
            border_x_right =  580
            border_x_left = 230
            border_y_up = 50
            border_y_down = 400
            if event.key == pygame.K_RIGHT and (game.player.rect.x != border_x_right and game.player.rect.x != border_x_left):
                game.player.move_right()
            elif event.key == pygame.K_LEFT and (game.player.rect.x != border_y_up and game.player.rect.x != border_x_left):
                game.player.move_left()
            elif event.key == pygame.K_UP:
                game.player.move_up()
            elif event.key == pygame.K_DOWN:
                game.player.move_down()
                
            
            
            