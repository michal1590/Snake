import random


class Snake:

    def __init__(self, map_size):
        self.map_size = map_size
        self.x_poz = int(random.random()*self.map_size)
        self.y_poz = int(random.random() * self.map_size)

