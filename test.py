import pygame
import time
import os

os.environ["SDL_VIDEODRIVER"] = "kmsdrm"

size = width, height = (1920, 1080)
pygame.init()
screen = pygame.display.set_mode(size)
screen.fill((30, 30, 30))

pygame.display.flip()
time.sleep(5)
