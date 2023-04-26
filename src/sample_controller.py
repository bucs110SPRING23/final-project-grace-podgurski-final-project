import pygame
import pygame_menu

from src.pilot import Pilot

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()

    self.screen = pygame.display.set_mode()
    size = pygame.display.get_window_size()

    self.width = size[0]
    self.height = size[1]

  def mainloop(self):
    #select state loop

  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
