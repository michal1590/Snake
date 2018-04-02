import snake as sn
import board as bd


class Game:

    def __init__(self, board_size):
        self.board = bd.Board(board_size)
        self.snake = sn.Snake(board_size)

        self.board.add_snake(self.snake.get_snake_head())
        self.board.show_board()

    def move(self):
        i = 0
        correct_direction = False
        while i < 5 and not correct_direction:
            direction = input("podaj kierunek ruchu: ")
            if direction in ['w', 's', 'a', 'd']:
                correct_direction = True
                self.snake.move(direction)
                break
            i += 1

        if not correct_direction:
            print('Game over!')

    def turn(self):
        self.move()
        self.board.start_new_board()
        self.board.add_snake(self.snake.get_snake_head())
        self.board.show_board()






