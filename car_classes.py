import pygame

big_car = pygame.image.load("images/cars/big_car.png")
medium_car = pygame.image.load("images/cars/medium_car.png")
small_car = pygame.image.load("images/cars/small_car.png")

class Car:
    def __init__(self, speed, x, y, health):
        #self.rect = pygame.Rect()
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.health_taken = 0
        self.direction = 'Forward'

    def move(self):
        if self.direction == 'Left':
            self.x = self.x + 0.5 * self.speed
        elif self.direction == 'Right':
            self.x = self.x - 0.5 *self.speed
        else:
            self.y = self.y + 0.5 * self.speed
            

    def die(self):
        pass

    def hit(self):
        pass


class Small_car(Car):
    def __init__(self, speed, x, y, health):
        super().__init__(speed, x, y, health)

    def draw(self, win):
        rectangle1 = pygame.Rect(self.x + 10, self.y - 30, self.health, 10)
        rectangle2 = pygame.Rect(self.x + 10, self.y - 30, self.health_taken, 10)

        if self.direction == 'Forward':
            rotated_image = pygame.transform.rotate(small_car, 0)
        elif self.direction == 'Left':
            rotated_image = pygame.transform.rotate(small_car, 90)
        else:
            rotated_image = pygame.transform.rotate(small_car, -90)

        win.blit(rotated_image, (self.x,self.y))
        pygame.draw.rect(win, (0,255,0), rectangle1)
        pygame.draw.rect(win, (255,0,0), rectangle2)

    def change_direction(self): # Left/Right/Forward
        if self.x == 217 and self.y > 190:
            self.direction = 'Left'
        elif self.x > 780  and self.y > 685:
            self.direction = 'Forward'
        elif self.x > 956 and self.y < 220:
            self.direction = 'Forward'
        elif self.x > 956 and self.y > 350:
            self.direction = 'Right'
        elif self.x < 490 and self.y > 685:
            self.direction = 'Left'
        elif self.x < 480 and self.y > 350:
           self.direction = 'Forward'


class Medium_car(Car):
    def __init__(self, speed, x, y, health):
        super().__init__(speed, x, y, health)

    def draw(self, win):
        rectangle1 = pygame.Rect(self.x + 15, self.y - 30, self.health, 10)
        rectangle2 = pygame.Rect(self.x + 15, self.y - 30, self.health_taken, 10)
        if self.direction == 'Forward':
            rotated_image = pygame.transform.rotate(medium_car, 0)
        elif self.direction == 'Left':
            rotated_image = pygame.transform.rotate(medium_car, 90)
        else:
            rotated_image = pygame.transform.rotate(medium_car, -90)
        win.blit(rotated_image, (self.x,self.y))

        pygame.draw.rect(win, (0,255,0), rectangle1)
        pygame.draw.rect(win, (255,0,0), rectangle2)

    def change_direction(self): # Left/Right/Forward
        if self.x == 190 and self.y > 159: # First turn
            self.direction = 'Left'
        elif self.x > 760  and self.y > 670: # Last Turn
            self.direction = 'Forward'
        elif self.x > 930 and self.y < 220: # Second Turn
            self.direction = 'Forward'
        elif self.x > 930 and self.y > 324: # Third Turn
            self.direction = 'Right'
        elif self.x < 490 and self.y > 670: # Fifth Turn
            self.direction = 'Left'
        elif self.x < 450 and self.y > 324: # Fourth Turn
           self.direction = 'Forward'

class Big_car(Car):
    def __init__(self, speed, x, y, health):
        super().__init__(speed, x, y, health)

    def draw(self, win):
        rectangle1 = pygame.Rect(self.x + 15, self.y - 30, self.health, 10)
        rectangle2 = pygame.Rect(self.x + 15, self.y - 30, self.health_taken, 10)

        if self.direction == 'Forward':
            rotated_image = pygame.transform.rotate(big_car, 0)
        elif self.direction == 'Left':
            rotated_image = pygame.transform.rotate(big_car, 90)
        else:
            rotated_image = pygame.transform.rotate(big_car, -90)
        win.blit(rotated_image, (self.x,self.y))
        pygame.draw.rect(win, (0,255,0), rectangle1)
        pygame.draw.rect(win, (255,0,0), rectangle2)

    def change_direction(self): # Left/Right/Forward
        if self.x == 193 and self.y > 165: # First turn
            self.direction = 'Left'
        elif self.x > 768  and self.y > 670: # Last Turn
            self.direction = 'Forward'
        elif self.x > 936 and self.y < 220: # Second Turn
            self.direction = 'Forward'
        elif self.x > 930 and self.y > 330: # Third Turn
            self.direction = 'Right'
        elif self.x < 490 and self.y > 670: # Fifth Turn
            self.direction = 'Left'
        elif self.x < 450 and self.y > 324: # Fourth Turn
           self.direction = 'Forward'
