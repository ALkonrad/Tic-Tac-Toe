game_board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-']


def draw_board():
    print(game_board[0] + game_board[1] + game_board[2])
    print(game_board[3] + game_board[4] + game_board[5])
    print(game_board[6] + game_board[7] + game_board[8])


def add_symbol(symbol):
    symbol_location = int(input('>>> ')) - 1
    game_board[symbol_location] = symbol
    draw_board()


current_symbol = 'x'
for turns in range(9):
    add_symbol(current_symbol)
    if current_symbol == 'x':
        current_symbol = 'o'
    else:
        current_symbol = 'x'
