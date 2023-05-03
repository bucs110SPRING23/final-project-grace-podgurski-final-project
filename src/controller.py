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
    menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('Amelia Earhart Flight Simulator Game')
    menu.add.button('Play', gameloop)
    menu.add.button('Quit', pygame_menu.events.EXIT)


  def gameloop(self):
    
    speed = 5
    arcade.open_window(self.width,self.height)
    background = arcade.set_background_color(arcade.color.BLUE)

    while True:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()

      screen.blit(background, (0,0))
      pygame.display.update()


    Pilot.move()



    

      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
    pass
      #event loop

      #update data

      #redraw
