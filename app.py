from game import Game


game = Game(5)
while not game.game_over:
    game.turn()
