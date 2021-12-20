import pygame
import math

cannon_images = []
mg_images = []
missile_launcher_images = []

tower_bg = pygame.image.load("images/towers/Tower.png")
tower_bg = pygame.transform.scale(tower_bg, (75, 75))

cannon1 = pygame.image.load("images/towers/Cannon.png")
cannon2 = pygame.image.load("images/towers/Cannon2.png")
cannon3 = pygame.image.load("images/towers/Cannon3.png")
cannon1 = pygame.transform.scale(cannon1, (41, 75))
cannon2 = pygame.transform.scale(cannon2, (41, 75))
cannon3 = pygame.transform.scale(cannon3, (41, 75))
cannon_images.extend([cannon1, cannon2, cannon3])



mg1 = pygame.image.load("images/towers/MG.png")
mg2 = pygame.image.load("images/towers/MG2.png")
mg3 = pygame.image.load("images/towers/MG3.png")
mg1 = pygame.transform.scale(mg1, (37, 75))
mg2 = pygame.transform.scale(mg2, (37, 75))
mg3 = pygame.transform.scale(mg3, (37, 75))
mg_images.extend([mg1, mg2, mg3])

missile_launcher1 = pygame.image.load("images/towers/Missile_Launcher.png")
missile_launcher2 = pygame.image.load("images/towers/Missile_Launcher2.png")
missile_launcher3 = pygame.image.load("images/towers/Missile_Launcher3.png")
missile_launcher1 = pygame.transform.scale(missile_launcher1, (45, 75))
missile_launcher2 = pygame.transform.scale(missile_launcher2, (45, 75))
missile_launcher3 = pygame.transform.scale(missile_launcher3, (45, 75))
missile_launcher_images.extend([missile_launcher1, missile_launcher2, missile_launcher3])

class Tower:
    def __init__(self, x,y, damage, speed, cost):
        self.x = x
        self.y = y
        self.damage = damage
        self.speed = speed
        self.cost = cost
        self.is_moved = False
        self.rotation = 0
        self.upgrade = 0

    def move(self, x, y):
        if not self.is_moved:
            self.x = x
            self.y = y

    def shoot(self):
        pass

    def rotate(self, x, y, length):
        if length == 0:
            if self.is_moved:
                mouse_x, mouse_y = x, y
                radians = math.atan2((mouse_y - self.y), (mouse_x - self.x))
                degs = radians * (180 / math.pi)
                self.rotation = degs
            self.rotation = 0

    def click_function(self):
        pass

    

class Cannon(Tower):
    def __init__(self, x, y, damage, speed, cost):
        super().__init__(x, y, damage, speed, cost)

    def draw(self, win):
        win.blit(tower_bg, (self.x - 37, self.y - 37))
        rotated_image = pygame.transform.rotate(cannon_images[self.upgrade], int(self.rotation))
        win.blit(rotated_image, (self.x - 20, self.y - 53))


class MG(Tower):
    def __init__(self, x, y, damage, speed, cost):
        super().__init__(x, y, damage, speed, cost)

    def draw(self, win):
        win.blit(tower_bg, (self.x - 37, self.y - 37))
        rotated_image = pygame.transform.rotate(mg_images[self.upgrade], int(self.rotation))
        win.blit(rotated_image, (self.x - 20, self.y - 53))

class Missile_Launcher(Tower):
    def __init__(self, x, y, damage, speed, cost):
        super().__init__(x, y, damage, speed, cost)

    def draw(self, win):
        win.blit(tower_bg, (self.x - 37, self.y - 37))
        rotated_image = pygame.transform.rotate(missile_launcher_images[self.upgrade],int(self.rotation))
        win.blit(rotated_image, (self.x - 23, self.y - 53))