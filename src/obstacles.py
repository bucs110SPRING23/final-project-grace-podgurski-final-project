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
        speed_cloud = 5
        self.left(speed_cloud)
