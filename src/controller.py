import pygame
import arcade
import pygame_menu

from src.pilot import Pilot

class Controller:
  
  def __init__(self,width,height):
    #setup pygame data
    self.screen = pygame.display.set_mode()
    size = pygame.display.get_window_size()

    self.width = size[0]
    self.height = size[1]


  def menuloop(self):
    arcade.open_window(self.width,self.height)
    background = arcade.set_background_color(arcade.color.BLUE)
    
    while True:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()

      screen.blit(background, (0,0))
      pygame.display.update()




  def gameloop(self):
    speed = 5

    

      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
    pass
      #event loop

      #update data

      #redraw
