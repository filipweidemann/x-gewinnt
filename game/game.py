"""
The class for
a game board.
"""
class Board:

    """ Constructor """
    def __init__(self, width, height, game_state=None, win=4):
        # creating instance variables
        self.width = int(width)
        self.height = int(height)
        self.win_length = int(win)
        self.count_tokens = 0
        self.game_status = 'active'
        self.turn_color = None
        self.won_by = None
        self.game_state = game_state

        # Checks if a game should be initialized using and empty
        # board or if an existing board should be loaded..
        # Then sets the board accordingly.
        if self.game_state is None:
            try:
                self.game_state = [['.' for _ in range(int(width))] for _ in range(int(height))]
            except ValueError:
                print('Wrong Values! Game is restarting.')

    def __getitem__(self, item):
        return item

    # make this class JSON serializable
    def serialize(self):
        return {
            'height': self.height,
            'width': self.width,
            'win_length': self.win_length,
            'count_tokens': self.count_tokens,
            'game_status': self.game_status,
            'game_state': self.game_state,
            'turn_color': self.turn_color,
            'won_by': self.won_by
        }

    """
    Generates a valid board using the provided ascii-string
    and returns that board.
    """
    @staticmethod
    def load(trimmed_ascii, win=3):
        height = len(trimmed_ascii.splitlines())-1
        width = max([len(line) for line in trimmed_ascii.strip().splitlines()[1:] if line != []])
        board = Board(width, height, win)
        board.game_state = [list(i) for i in trimmed_ascii.splitlines()]
        board.game_state.remove([])
        board.win_length = win
        winner = board.check_winner()
        if winner != None:
            board.won_by = winner
        return board
    
    """
    Can be called anytime to print a version
    of the current board.
    """
    def ascii(self):
        # Initialize the base string (which will be returned)
        # to start in the next line by default (hence the '\n').
        return_string = '\n'
        # Loops through the game_state array
        for element in self.game_state:
            # Loops through the characters in the array.
            for sub_element in element:
                # Adds every character of a single line respectively,
                # then terminates...
                return_string += sub_element
            # ...and adds a new line to the string.
            return_string += '\n'
        # Finally, return the full ascii representation!
        return return_string


    """
    Returns an array / list of all axis combinations
    starting at the specified point (x/y).
    """
    def axis_strings(self, x, y):
        # Initialize an array for all 4 axis string.
        axis_array = ['', '', '', '']
        temp = ''
        for i in range(x, self.width):
            if i == x:
                for j in range(y, self.height):
                    temp += self.game_state[self.height - 1 - j][i]
                axis_array[0] = temp
                temp = ''
                for cnt in range(1, 3):
                    dx = x
                    dy = y
                    if cnt == 1:
                        for l in range(x, self.width):
                            if dy < self.height:
                                temp += self.game_state[self.height - 1 - dy][dx]
                                dx += 1
                                dy += 1
                        axis_array[2] = temp
                        dx = x
                        dy = y
                    else:
                        temp = ''
                        for l in range(x, -1, -1):
                            if l >= 0:
                                temp += self.game_state[self.height - 1 - dy][dx]
                                dx -= 1
                                dy += 1
                        axis_array[1] = temp
                        temp = ''

            temp += self.game_state[self.height - 1 - y][i]
        axis_array[3] = temp
        return axis_array

    """
    Checks the current state of the board and
    (if exists) locks the game and returns
    the winner.
    """
    def check_winner(self):
        winner = None
        for i in range(0, self.width):
            for j in range(0, self.height):
                if i == 0:
                    curr_axis = self.axis_strings(i, j)
                else:
                    curr_axis = self.axis_strings(j, i)
                for line in curr_axis:
                    if 'x' * self.win_length in line:
                        winner = 'x'
                        break
                    if 'o' * self.win_length in line:
                        winner = 'o'
                        break
        return winner


    """
    Drops a token with the specfied color in a row.
    """
    def drop(self, drop_color, drop_row):
        # Checks if it's the first turn.
        # If not, checks if the correct color has been dropped,
        # otherwise throws an exception.
        if self.turn_color is None or drop_color == self.turn_color:
            # If the current player has dropped a token,
            # change the drop_color to the other player.
            if drop_color == 'x': self.turn_color = 'o'
            if drop_color == 'o': self.turn_color = 'x'
            # Iterate through the selected row and
            # determine where the new token will stop.
            # TODO:
            # let tokens fall off (not register them) when a row is already full!
            for i in range(0, int(self.height)):
                if self.game_state[int(self.height)-1-i][drop_row] == '.':
                    self.game_state[int(self.height)-1-i][drop_row] = drop_color
                    position = (drop_row, i)
                    dropped_token = Token(drop_color, position)
                    self.count_tokens += 1

                    # check for win
                    winner = self.check_winner()
                    if winner != None:
                        self.game_status = 'over'
                        self.won_by = winner

                    return dropped_token

            return Token(drop_color, (-1, -1))


        else:
            raise Exception('It\'s not your turn yet!')

        return Token(drop_color, (-1, -1))

"""
The class for tokens.
"""
class Token:
    def __init__(self, color, position):
        self.color = color
        self.position = position
