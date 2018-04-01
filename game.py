import snake as sn
import board as bd


class Game:

    def __init__(self, board_size):
        self.board = bd.Board(board_size)
        self.snake = sn.Snake(board_size)

#        self.board.fill_board()
        self.board.add_snake(self.snake.get_snake_head())

        self.board.show_board()







