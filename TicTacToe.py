game_board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-']


def draw_board():
    print(game_board[0] + game_board[1] + game_board[2])
    print(game_board[3] + game_board[4] + game_board[5])
    print(game_board[6] + game_board[7] + game_board[8])

# This code takes an imput from one to nine and adds a symbol in that square


def add_symbol(symbol):
    symbol_location = int(input('>>> ')) - 1
    # Checks if the number entered is greater than 9
    if symbol_location > 8:
        print('The number you have entered is too large.')
        add_symbol(symbol)
        # checks if the square is takenjjj
    elif game_board[symbol_location] != '-':
        print('This square is taken.')
        add_symbol(symbol)
    else:
        game_board[symbol_location] = symbol
        draw_board()
        check_if_won()


def check_if_won():
    winning_combinations = [
        # Checks rows
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # Checks colums
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # Checks diagonals
        [0, 4, 8], [2, 4, 6],
    ]
    for current_combination in winning_combinations:
        # Checks if x won
        if game_board[current_combination[0]] == game_board[current_combination[1]] == game_board[current_combination[2]] == 'x':
            print('x wins')
            exit()
            # Checks if o won
        elif game_board[current_combination[0]] == game_board[current_combination[1]] == game_board[current_combination[2]] == 'o':
            print('o wins')
            exit()


# Switches between x and o while looping through the board
current_symbol = 'x'
for turns in range(9):
    add_symbol(current_symbol)
    if current_symbol == 'x':
        current_symbol = 'o'
    else:
        current_symbol = 'x'
