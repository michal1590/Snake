class Board:

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [['*']*self.board_size for x in range(self.board_size)]

    def start_new_board(self):
        self.board = [['*']*self.board_size for x in range(self.board_size)]

    def show_board(self):
        #os.system('cls')
        print('\n')
        for row in self.board:
            row_str = ' '.join(row)
            print(row_str)

    def add_snake(self, snake_pos):
        self.board[snake_pos[1]][snake_pos[0]] = 'X'

    def add_cookie(self, cookie_pos):
        self.board[cookie_pos[1]][cookie_pos[0]] = '@'
