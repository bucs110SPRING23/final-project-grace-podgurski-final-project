import pygame
import arcade

class Controller:
  
  def __init__(self,width,height):
    self.screen = pygame.display.set_mode()
    size = pygame.display.get_window_size()

    self.width = size[0]
    self.height = size[1]

    arcade.open_window(self.width,self.height)
    arcade.set_background_color(arcade.color.BLUE)

    