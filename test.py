import pygame
import time

# PyGame
size = width, height = (800, 480)
pygame.init()
screen = pygame.display.set_mode(size) # , pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
screen.fill((60, 60, 60))

CENTER_X, CENTER_Y = (width / 2, height / 2)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font_60 = pygame.font.SysFont("dejavusans", 60)
counter1 = 0
loop = True

while loop:
    counter1 += 1
    pygame.draw.rect(screen, BLACK, [CENTER_X - 150, 180, 300, 150], border_radius=10)
    counter2 = font_60.render(str(counter1),True, WHITE, BLACK)
    screen.blit(counter2, (CENTER_X - 20, CENTER_Y - 20))
    pygame.display.flip()
    time.sleep(1)
    if counter1 == 20:
        pygame.quit()
        loop = False
