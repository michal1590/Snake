import snake as sn
import board as bd
import cookies as ck


class Game:

    def __init__(self, board_size):
        self.game_over = False
        self.board_size = board_size

        self.board = bd.Board(board_size)
        self.snake = sn.Snake(board_size)
        self.cookie = ck.Cookie(board_size)

        self.board.add_snake(self.snake.get_snake_head())
        self.generate_cookie()
        self.board.add_cookie(self.cookie.get_cookie())

        self.board.show_board()

    def generate_cookie(self):
        while self.check_cookie_and_snake():
            self.cookie.new_cookie()

    def check_cookie_and_snake(self):
        (x_cookie, y_cookie) = self.cookie.get_cookie()
        (x_snake, y_snake) = self.snake.get_snake_head()
        if x_cookie == x_snake and y_cookie == y_snake:
            return True
        else:
            return False

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
            self.game_ends()

    def turn(self):
        self.move()
        self.board.start_new_board()

        self.board.add_snake(self.snake.get_snake_head())
        if self.check_cookie_and_snake():
            self.generate_cookie()
        self.board.add_cookie((self.cookie.get_cookie()))

        self.board.show_board()

    def game_ends(self):
        self.game_over = True






