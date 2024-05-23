import time
import pygame

from Model.House import House

pygame.init()


def main():
    pygame.display.set_mode((600,400))
    pygame.display.set_caption("House")
    fl_running = True
    clock = pygame.time.Clock()
    while fl_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                fl_running = False
        clock.tick(60)
    print("Молодец")
    house = House(height=400, max_of_floors=10)


main()

