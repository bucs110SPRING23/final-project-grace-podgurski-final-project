import pygame
import arcade
import pygame_menu

from src.pilot import Pilot
from src.obstacles import Obstacles

class Controller:
  
  def __init__(self,screen,width,height):
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


  def gameloop(self,result):
    arcade.open_window(self.width,self.height)
    background = arcade.set_background_color(arcade.color.BLUE)


    while self.state == "GAME":
      result = "null"
      hit = pygame.sprite.spritecollide(Pilot,Obstacles)
      avoiding = 3

      # To check that the player is in the screen
      if self.left < 0:
          self.left = 0
      elif self.right > Controller.width - 1:
          self.right = Controller.width - 1

      if self.bottom < 0:
          self.bottom = 0
      elif self.top > Controller.height - 1:
          self.top = Controller.height - 1

    # Check if distance is reached
      if Pilot.distance < 1700:
        Pilot.update_pos()
      elif Pilot.distance >= 1700:
        Controller.gameoverloop(result="win")
    
      for event in pygame.event.get():
        if Pilot.move.up == True:
          Pilot.control(0, avoiding)
        elif Pilot.move.down == True:
          Pilot.control(0, -avoiding)
        elif hit == True:
          result = "loss"
          Controller.gameoverloop(result = "loss")

          self.sprites.update()
          pygame.display.update()
    return result

    
    
  def gameoverloop(self, win, loss):
    for _ in Controller.gameloop():
      if result == "loss":
        disp = pygame.image.load("/Users/gracepodgurski/Documents/GitHub/final-project-grace-podgurski-final-project/assets/loss_screen.png")
        Controller.screen.blit(disp,(0,0))
        pygame.display.update()
        pygame.quit()
      elif result == "win":
        disp = pygame.image.load("/Users/gracepodgurski/Documents/GitHub/final-project-grace-podgurski-final-project/assets/win_screen.png")
        Controller.screen.blit(disp,(0,0))
        pygame.display.update()
        pygame.quit()
