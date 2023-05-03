import pygame
import arcade
import pygame_menu
import controller
import pilot

def main():
    pygame.init()
    game = controller.Controller()
    game.mainloop()

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
