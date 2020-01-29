import pygame
import os

class Display():
    def show(self):
        # Define some colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        GRAY = (80, 80, 80)
        GREEN = (0,255,0)

        WIDTH = 25
        HEIGHT = 25

        MARGIN = 1

        pygame.init()

        WINDOW_SIZE = [416, 416]
        screen = pygame.display.set_mode(WINDOW_SIZE)

        done = False

        clock = pygame.time.Clock()

        while not done:
            with open('board.txt') as fp:
                grid = fp.readline().strip(',').split(',')
                if grid == ['']:
                    continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            # Draw the grid
            for row in range(16):
                for column in range(16):
                    color = WHITE
                    if grid[row][column] == 'W':
                        color = RED
                    elif grid[row][column] == 'B':
                        color = GRAY
                    elif grid[row][column] == 'T':
                        color = GREEN
                    pygame.draw.rect(screen, color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH, HEIGHT])
            clock.tick(60)
            pygame.display.flip()
        pygame.quit()

if __name__ == '__main__':
    Display().show()
    # os.system('python homework3.py')