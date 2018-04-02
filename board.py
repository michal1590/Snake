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

    def add_snake(self, snake_poz):
        self.board[snake_poz[1]][snake_poz[0]] = 'X'
