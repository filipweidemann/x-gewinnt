import game

def main():
    loading = None
    while(loading != 'y' and loading != 'n'):
        loading = input('Load savegame? (y/n): ')
    if loading != 'y':
        print('NEW GAME ')
        width = input('Width of the board: ')
        height = input('Height of the board: ')
        win = input('# of tokens in a row to claim the win: ')
        starting_player = None
        while(starting_player != 'x' and starting_player != 'o'):
            starting_player = input('Who want\'s to start? x or o? ')
        new_game = game.Board(int(width), int(height), None, int(win))

    #TODO: load game out of file -> implement a save function
    #TODO  that writes game.ascii() to a file.
    else:
        pass

    new_game.turn_color = starting_player
    while(new_game.game_status == 'active'):
        print('\n')
        print('The board:')
        print(new_game.ascii())
        print('Player ' + new_game.turn_color + '\'s turn!')
        row = int(input('Select your row: '))
        new_game.drop(new_game.turn_color, row)
    print('Game finished! ')
    print('***THE WINNER***')
    print('******* ' + new_game.won_by + ' ******')

# game loop goes here
if __name__ == '__main__':
    main()
