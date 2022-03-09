# Seth Whetten
# 01 Prove Assignment - Tic Tac Toe
# CSE 210

def main():
    print('--------------------------------------------------\n')

    is_playing = True
    players = ['x', 'o']
    player_playing = 1
    grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    turn = 0

    print_grid(grid)

    while is_playing:
        player_playing = (player_playing + 1) % 2
        turn += 1

        choice = input(f'{players[player_playing]}\'s turn to choose a square (1-9): ')
        number_valid = is_number_valid(choice)
        if number_valid:
            new_grid = update_grid(grid, int(choice), players[player_playing])
            if not new_grid:
                print('That spot is already taken')
            else:
                grid = new_grid
                print_grid(f'\n{grid}')
                
                is_playing = check_game(grid, players[player_playing], turn)
        else:
            print('Invalid entry: please enter a number between 1-9')

    print('\n--------------------------------------------------')

def is_number_valid(number):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return True if number.isdigit and int(number) in numbers else False

def game_over(winner = ''):
    print(f'{winner} wins!') if winner else print('Draw')

def check_game (grid, player, turn):
    win_possibilities = [
        [1, 4, 7],
        [3, 4, 5],
        [0, 4, 8],
        [2, 4, 6],
        [0, 1, 2],
        [0, 3, 7],
        [2, 5, 8],
        [6, 7, 8],
    ]

    for item in win_possibilities:
        if grid[item[0]] == grid[item[1]] == grid[item[2]] == player:
            game_over(player)
            return False
    if turn < 9:
        return True 
    else:
        game_over()
        return False

def update_grid(grid, new_entry, player):
    if grid[new_entry - 1] == str(new_entry):
        grid[new_entry - 1] = player
        return grid
    else:
        return False

def print_grid(new_grid = False):
    if not new_grid:
        new_grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    grid_text = ['', '', '']
    grid_spacer = '-+-+-'
    result = ''
    for i in range(len(grid_text)):
        for j in range(3):
            grid_text[i] += new_grid[j + (3*i)]
            if j < 2:
                grid_text[i] += '|'
        result += grid_text[i] + '\n'
        if i < 2:
            result += grid_spacer + '\n'

    print(result)


if __name__ == '__main__':
    main()
