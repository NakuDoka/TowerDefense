import pygame
import car_classes as car

WIDTH = 1200
HEIGHT = 1500
bg = pygame.image.load("images/bg.png")
bg = pygame.transform.scale(bg, (1200, 1200))
WIN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Tower Defense")
FPS = 30

cars = []
towers = []

cars.append(car.Small_car(30, 217, 0, 10))
cars.append(car.Medium_car(20, 190, 0, 10))
cars.append(car.Big_car(10, 193, 0, 10))




def redrawGameWindow():
    WIN.blit(bg, (0,0))
    for car in cars:
        car.draw(WIN)
    for tower in towers:
        tower.draw(WIN)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

        for car in cars:
            car.move()
            car.change_direction()
        
        redrawGameWindow()
    pygame.quit()
main()