import pygame
import arcade

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, x, y, img="assets/cloud.png"):
        super().__init__()

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def floating(self):
        

# add in sprite groups  in controller using:
# starting_clouds = 2
# interval = self.width/(starting_clouds+1)
# xpos = interval
# for _ in range(starting_clouds):
#     new_sm = Snowman(xpos, self.height/2)
#     self.clouds.add(new_sm)
#     xpos += interval