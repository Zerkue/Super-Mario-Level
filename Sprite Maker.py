# Imports
import pygame
from pygame import *

# Screen Dimensions

WIN_WIDTH = 1400
WIN_HEIGHT = 1000

# Screen Defaults

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0

# Spritesheet

spritesheet = pygame.image.load("resources/graphics/item_objects.png")


# Main Function

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Sprite Mapper")
    x = 0
    y = 0
    w = 100
    h = 50
    pygame.key.set_repeat(1, 30)
    f = open("test.txt", "w")
    f.close()

    while 1:
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit("ESCAPE")
            if e.type == KEYDOWN and e.key == K_DOWN:
                y = y - 1
            if e.type == KEYDOWN and e.key == K_UP:
                y = y + 1
            if e.type == KEYDOWN and e.key == K_RIGHT:
                x = x - 1
            if e.type == KEYDOWN and e.key == K_LEFT:
                x = x + 1
            if e.type == KEYDOWN and e.key == K_g:
                y = y - 10
            if e.type == KEYDOWN and e.key == K_t:
                y = y + 10
            if e.type == KEYDOWN and e.key == K_h:
                x = x - 10
            if e.type == KEYDOWN and e.key == K_f:
                x = x + 10
            if e.type == KEYDOWN and e.key == K_w:
                h = h - 1
            if e.type == KEYDOWN and e.key == K_s:
                h = h + 1
            if e.type == KEYDOWN and e.key == K_a:
                w = w - 1
            if e.type == KEYDOWN and e.key == K_d:
                w = w + 1
            if e.type == KEYDOWN and e.key == K_SPACE:
                name = input("Name of Sprite?")

                f = open("test.txt", "a")

                savedcode = ("character = Surface((") + str(w) + (",") + str(h) + ("),pygame.SRCALPHA)") + ("\n")
                f.write(savedcode)

                savedcode = ("character.blit(spritesheet,(") + str(x) + (",") + str(y) + ("))") + ("\n")
                f.write(savedcode)

                savedcode = ("character = pygame.transform.scale(character, (") + str(w) + (",") + str(h) + ("))") + (
                    "\n")
                f.write(savedcode)

                savedcode = name + (" = character") + ("\n") + ("\n")
                f.write(savedcode)

                f.close()

        screen.fill(Color("#2E722A"))

        character = Surface((w, h))
        character.fill(Color("#4CCCFF"))

        character.blit(spritesheet, (x, y))
        character = pygame.transform.scale(character, (w * 8, h * 8))
        screen.blit(character, (0, 0))

        pygame.display.update()


if __name__ == "__main__":
    main()