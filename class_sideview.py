import pygame
from pygame import draw

tower_bg = pygame.image.load("images/towers/Tower.png")
tower_bg = pygame.transform.scale(tower_bg, (175, 175))

cannon1 = pygame.image.load("images/towers/Cannon.png")
cannon2 = pygame.image.load("images/towers/Cannon2.png")
cannon3 = pygame.image.load("images/towers/Cannon3.png")
cannon1 = pygame.transform.scale(cannon1, (96, 175))
cannon2 = pygame.transform.scale(cannon2, (96, 175))
cannon3 = pygame.transform.scale(cannon3, (96, 175))


mg1 = pygame.image.load("images/towers/MG.png")
mg2 = pygame.image.load("images/towers/MG2.png")
mg3 = pygame.image.load("images/towers/MG3.png")
mg1 = pygame.transform.scale(mg1, (84, 175))
mg2 = pygame.transform.scale(mg2, (84, 175))
mg3 = pygame.transform.scale(mg3, (84, 175))

missile_launcher1 = pygame.image.load("images/towers/Missile_Launcher.png")
missile_launcher2 = pygame.image.load("images/towers/Missile_Launcher2.png")
missile_launcher3 = pygame.image.load("images/towers/Missile_Launcher3.png")
missile_launcher1 = pygame.transform.scale(missile_launcher1, (106, 175))
missile_launcher2 = pygame.transform.scale(missile_launcher2, (106, 175))
missile_launcher3 = pygame.transform.scale(missile_launcher3, (106, 175))

tower_cost = {
    'Canon': {
        1 : 50,
        2: 100,
        3: 150
    },
    'MG': {
        1 : 75,
        2: 150,
        3: 250
    },
    'Missile_Launcher': {
        1: 150,
        2: 300,
        3: 450
    }
}


class Sideview():
    def __init__(self):
        self.is_on = 'Normal' # Normal, Cannon, MG, Missile_Launcher
        self.gold = 0
        self.round = 1
        self.is_moving = False

    def click_function(self,pos):
        if 1250 < pos[0] < 2450:
            if 100 < pos[1] < 300:
                return self.is_on, 0
            elif 400 < pos[1] < 600:
                return self.is_on, 1
            elif 700 < pos[1] < 900:
                return self.is_on, 2
        return None, None

                
    def draw_boxes(self, win):
        rectangle1 = pygame.Rect(1250, 100, 200, 200)
        rectangle2 = pygame.Rect(1250, 400, 200, 200)
        rectangle3 = pygame.Rect(1250, 700, 200, 200)

        pygame.draw.rect(win, (0,0,0), rectangle1, 2)
        pygame.draw.rect(win, (0,0,0), rectangle2, 2)
        pygame.draw.rect(win, (0,0,0), rectangle3, 2)

    def draw_normal(self,win):
        win.blit(tower_bg, (1266, 112))
        win.blit(cannon1, (1305, 72))
        win.blit(tower_bg, (1266, 412))
        win.blit(mg1, (1305, 372))
        win.blit(tower_bg, (1266, 712))
        win.blit(missile_launcher1, (1305, 672))

    def draw_cannons(self,win):
        win.blit(tower_bg, (1266, 112))
        win.blit(cannon1, (1305, 72))
        win.blit(tower_bg, (1266, 412))
        win.blit(cannon2, (1305, 372))
        win.blit(tower_bg, (1266, 712))
        win.blit(cannon3, (1305, 672))

    def draw_mg(self,win):
        win.blit(tower_bg, (1266, 112))
        win.blit(mg1, (1305, 72))
        win.blit(tower_bg, (1266, 412))
        win.blit(mg2, (1310, 372))
        win.blit(tower_bg, (1266, 712))
        win.blit(mg3, (1305, 672))

    def draw_missile_launcher(self,win):
        win.blit(tower_bg, (1266, 112))
        win.blit(missile_launcher1, (1300, 72))
        win.blit(tower_bg, (1266, 412))
        win.blit(missile_launcher2, (1300, 372))
        win.blit(tower_bg, (1266, 712))
        win.blit(missile_launcher3, (1300, 672))


    def draw(self, win): # 1200 * 300
        self.draw_boxes(win)
        if self.is_on == 'Normal':
            self.draw_normal(win)
        elif self.is_on == 'Cannon':
            self.draw_cannons(win)
        elif self.is_on == 'MG':
            self.draw_mg(win)
        elif self.is_on == 'Missile_Launcher':
            self.draw_missile_launcher(win)

