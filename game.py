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
        check = False  # is there intersection

        (x_cookie, y_cookie) = self.cookie.get_cookie()
        (x_snake, y_snake) = self.snake.get_snake_head()

        if x_cookie == x_snake and y_cookie == y_snake:
            check = True
        if self.snake.length > 0:
            for section in self.snake.tail:
                (x_snake, y_snake) = section
                if x_cookie == x_snake and y_cookie == y_snake:
                    check = True
        return check

    def check_snake_and_tail(self):
        check = False
        (x_head, y_head) = self.snake.get_snake_head()
        if self.snake.length > 0:
            for section in self.snake.tail:
                (x_tail, y_tail) = section
                if x_head == x_tail and y_head == y_tail:
                    check = True
                    self.game_ends()
                    break
        return check

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
            self.game_ends()

    def turn(self):
        self.move()
        self.check_snake_and_tail()

        self.board.start_new_board()

        if self.check_cookie_and_snake():
            self.generate_cookie()
            self.snake.feed()

        self.board.add_cookie(self.cookie.get_cookie())
        if self.snake.length > 0:
            self.board.add_tail(self.snake.tail)
        self.board.add_snake(self.snake.get_snake_head())

        self.board.show_board()

    def game_ends(self):
        print(f'Game over! Snake length is {self.snake.length}')
        self.game_over = True






