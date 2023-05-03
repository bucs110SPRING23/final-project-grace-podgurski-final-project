import pygame
import arcade

pygame.init()
screen = pygame.display.set_mode()
size = pygame.display.get_window_size()

width = size[0]
height = size[1]

arcade.open_window(width,height)
screen.fill("blue")
# arcade.set_background_color(arcade.color.BLUE)
pygame.display.flip()
pygame.time.wait(2000)

    

