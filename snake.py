import random
import board


class Snake:

    def __init__(self, map_size):
        self.map_size = map_size
        self.x_poz = int(random.random()*self.map_size)
        self.y_poz = int(random.random() * self.map_size)

    def get_snake_head(self):
        return self.x_poz, self.y_poz

    def add_snake_to_map(self):
        x = self.snake_poz[0]
        y = self.snake_poz[1]
        self.board[x][y] = '@'
