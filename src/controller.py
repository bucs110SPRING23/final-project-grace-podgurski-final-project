import pygame
import arcade
import pygame_menu

from src.pilot import Pilot
from src.obstacles import Obstacles

class Controller:
  
  def __init__(self,width,height):
    #setup pygame data
    self.screen = pygame.display.set_mode()
    size = pygame.display.get_window_size()

    screen =  self.screen

    self.width = size[0]
    self.height = size[1]

    return screen, width, height


  def menuloop(self):
    menu = pygame_menu.Menu('Welcome', 400, 300,theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('Amelia Earhart Flight Simulator Game')
    menu.add.button('Play', Controller.gameloop())
    menu.add.button('Quit', pygame_menu.events.EXIT)


  def gameloop(self):
    
    speed = 5
    speedx =  100
    speedy = 120
    arcade.open_window(self.width,self.height)
    background = arcade.set_background_color(arcade.color.BLUE)


    while self.state == "GAME":

        for event in pygame.event.get():
            if self.obstacles.rect.collidepoint(event.pos):
                pygame.quit()
                exit()

        self.sprites.update()
    # while True:
    #   for event in pygame.event.get():
    #     if event.type == QUIT:
    #       pygame.quit()
    #       gameoverloop()
    #     elif event.type = 




    pygame.display.update()


    Pilot.move()

      #event loop

      #update data - add 100 miles each frame 
      

      #redraw
    # for event in pygame.event.get():
    #   if collision 
    #     result = loss
    #    elif distance = 5000
    #      result = win
          
    # End the program when distance = 5000 (representing approximately 5000 miles of the Atlantic Ocean)

    
  def gameoverloop(self):
    for event in pygame.event.get():

      #event loop

      #update data

      #redraw
