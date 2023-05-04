import pygame
import arcade
import math

class Pilot(arcade.Sprite):
  starting_point = int[50,50]
  scale = 0.5

  def __init__(self, x, y, img="assets/cloud.png"):
      super().__init__()

      self.image = pygame.image.load(img)
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y

### Update position of the player - always moving right with time

  def update_pos(self):
    distance = [0]
    speed = 10
    self.right(speed)
    distance = distance + speed
    
# To check that the player is in the screen
    if self.left < 0:
        self.left = 0
    elif self.right > controller.width - 1:
        self.right = controller.width - 1

    if self.bottom < 0:
        self.bottom = 0
    elif self.top > controller.height - 1:
        self.top = controller.height - 1

  def move(self,speed):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          Pilot.move.up = True
          Pilot.move.down = False
        if event.key == pygame.K_DOWN:
          Pilot.move.up = False
          Pilot.move.down = True
        
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
          Pilot.update_pos()
        if event.key == pygame.K_DOWN:
          Pilot.update_pos()
     
  
  
