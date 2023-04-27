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
     pass
  
  def move_down(self):
     pass
  
  
