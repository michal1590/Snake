import random
import board


class Snake:

    def __init__(self, map_size):
        self.map_size = map_size
        self.x_poz = int(random.random() * self.map_size)
        self.y_poz = int(random.random() * self.map_size)
        self.length = 0
        self.tail = []

    def get_snake_head(self):
        return self.x_poz, self.y_poz

    def move(self, direction):
        if self.length > 0:
            for section in range(self.length-1, 0, -1):
                print(section)
                self.tail[section] = self.tail[section-1]
            self.tail[0] = self.get_snake_head()

        if direction == 's' and self.y_poz + 1 < self.map_size:
            self.y_poz += 1
        if direction == 'w' and self.y_poz - 1 >= 0:
            self.y_poz -= 1
        if direction == 'a' and self.x_poz - 1 >= 0:
            self.x_poz -= 1
        if direction == 'd' and self.x_poz + 1 < self.map_size:
            self.x_poz += 1

    def feed(self):
        self.length += 1
        self.tail.insert(0, self.get_snake_head())
