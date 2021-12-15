

class Tower:
    def __init__(self, x,y, damage, speed, cost):
        self.x = x
        self.y = y
        self.damage = damage
        self.speed = speed
        self.cost = cost
        self.is_moved = False

    def move(self, x, y):
        self.x = x
        self.y = y

    def shoot(self):
        pass

    

