import pygame
import car_classes as car
from class_sideview import Sideview
from tower_classes import MG, Cannon, Missile_Launcher

WIDTH = 1500
HEIGHT = 1200
bg = pygame.image.load("images/bg.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")
FPS = 30

cars = []
towers = []
sideview = Sideview()

cars.append(car.Small_car(30, 217, 0, 80))
#cars.append(car.Medium_car(20, 190, 0, 100))
#cars.append(car.Big_car(10, 193, 0, 120))

def spawn_tower(what_tower, index, pos):
    all_towers = [Cannon, MG, Missile_Launcher]
    print(what_tower)
    if what_tower == 'Normal':
        towers.append(all_towers[index](pos[0], pos[1], 10, 10, 80))



def redrawGameWindow():
    WIN.blit(bg, (0,0))
    sideview.draw(WIN)
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
                if sideview.is_moving:
                    towers[-1].is_moved = True
                    sideview.is_moving = False
                else:
                    what_tower, index = sideview.click_function(pos)
                    if what_tower:
                        sideview.is_moving = True
                        spawn_tower(what_tower, index, pos)

            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                for tower in towers:
                    if not tower.is_moved:
                        tower.move(pos[0], pos[1])



        for car in cars:
            car.move()
            car.change_direction()

        for tower in towers:
            tower.rotate(cars[0].x, cars[0].y)

        
        
        redrawGameWindow()
    pygame.quit()
main()