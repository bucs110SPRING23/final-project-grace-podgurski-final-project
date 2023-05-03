import pygame
import arcade
import controller

class Pilot:
  starting_score = 0
  starting_point = int[0,0]

  def __init__(self,x,y,shape):
    self.x = x
    self.y = y
    self.shape = arcade.Sprite(":assets/plane_image.png")

### Update position of the player - always moving right with time

  def update_pos(self):
    self.x += self.change_x
    self.y += self.change_y

# To check that the player is in the screen
    if self.left < 0:
        self.left = 0
    elif self.right > controller.width - 1:
        self.right = controller.width - 1

    if self.bottom < 0:
        self.bottom = 0
    elif self.top > controller.height - 1:
        self.top = controller.height - 1

  def move(self):
    # pressing arrow makes you move at a 45 degree angle in that direction
    # In testing phase right now but will be updated later
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          print("up")
        if event.key == pygame.K_DOWN:
           print("Down")
        
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
          print("Up STOP")
        if event.key == pygame.K_DOWN:
           print("Down STOP")
     
  
  
