import pygame

class Pilot:
  starting_score = 0
  starting_point = int[0,0]

  def __init__(self,x,y,shape,size,color):
    self.x = x
    self.y = y
    self.shape = shape
    self.size = size
    self.direction = "right"
    self.color = color

  def move_right(self):
    if self.direction == "right":
        self.x -= 1
    else:
        self.x += 1

  def move_up(self):
    #  pressing up arrow makes you move up at a 45 degree angle
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
     
  
  def move_down(self):
    #  pressing down arrow makes you move down at a 45 degree angle
     pass
  
  
