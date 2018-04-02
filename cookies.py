import random


class Cookie:

    def __init__(self, map_size):
        self.map_size = map_size
        self.x_poz = int(random.random() * self.map_size)
        self.y_poz = int(random.random() * self.map_size)

    def get_cookie(self):
        return self.x_poz, self.y_poz

    def new_cookie(self):
        self.x_poz = int(random.random() * self.map_size)
        self.y_poz = int(random.random() * self.map_size)
