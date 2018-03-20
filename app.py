import random
import os


class Snake:

    def __init__(self, map_size):
        self.map_size = map_size
        self.x_poz = int(random.random()*self.map_size)
        self.y_poz = int(random.random() * self.map_size)


class Game:

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = self.start_new_board()
        self.snake = self.create_snake()
        self.snake_poz = self.get_snake_head()

    def start_new_board(self):
        return [['*']*self.board_size for x in range(self.board_size)]

    def show_board(self):
        #os.system('cls')
        print('\n')
        for row in self.board:
            row_str = ' '.join(row)
            print(row_str)

    def create_snake(self):
        return Snake(self.board_size)

    def get_snake_head(self):
        return self.snake.x_poz, self.snake.y_poz

    def add_snake_to_map(self):
        x = self.snake_poz[0]
        y = self.snake_poz[1]
        self.board[x][y] = '@'


########################################################################################################################
########################################################################################################################
########################################################################################################################


game = Game(5)
game.show_board()
game.add_snake_to_map()
game.show_board()
