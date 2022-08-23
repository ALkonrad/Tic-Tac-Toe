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
    if symbol_location > 8:
        print('The number you have entered is too large.')
        add_symbol(symbol)
    elif game_board[symbol_location] != '-':
        print('This square is taken.')
        add_symbol(symbol)
    else:
        game_board[symbol_location] = symbol
        draw_board()
        check_if_won()


def check_if_won():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
    ]
    for current_combination in winning_combinations:
        if game_board[current_combination[0]] == game_board[current_combination[1]] == game_board[current_combination[2]] == 'x':
            print('x wins')
            exit()
        elif game_board[current_combination[0]] == game_board[current_combination[1]] == game_board[current_combination[2]] == 'o':
            print('o wins')
            exit()


current_symbol = 'x'
for turns in range(9):
    add_symbol(current_symbol)
    if current_symbol == 'x':
        current_symbol = 'o'
    else:
        current_symbol = 'x'
