import pygame
import arcade
import pygame_menu

from src.pilot import Pilot

class Controller:
  
  def __init__(self,width,height):
    #setup pygame data
    pygame.init()

    self.screen = pygame.display.set_mode()
    size = pygame.display.get_window_size()

    self.width = size[0]
    self.height = size[1]

    arcade.open_window(self.width,self.height)
    arcade.set_background_color(arcade.color.BLUE)

  def menuloop(self):
    pass
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    pass
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
    pass
      #event loop

      #update data

      #redraw
