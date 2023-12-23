import time
from Player import HumanPlayer, RandomCompPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # Single list to create 3x3 board 
        self.current_winner = None # Keep track of winner

    def print_board(self):
        '''
        This function is gettin the rows.
        Indices 0-2 is first row 
        Indices 3-5 is second row 
        Indices 6-8 is third row 
        '''
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    @staticmethod
    def print_board_nums():
        '''
        0 | 1 | 2 etc (tells us what number corresponds to what box)
        '''
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board: 
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board # This will return empty spaces in boolean.
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # If valid move, then make the move (assign square to letter) then return True.
        # If invalid, return False.
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Winner is 3 in a row, we have to check all of these.
        # First let's check the row.
        row_ind = square // 3 
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check column. 
        col_ind = square % 3
        column =[self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonal. 
        # Intuitively, you can win a diagonal if 
        # the square is an even number (0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # Left to right diagonal 
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # Top right to bottom legt diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        # If all of these fail..
        return False

def play(game, x_player, o_player, print_game=True):
    '''
    Returns the winner of the game. Otherwise None for a tie.
    '''
    if print_game:
        game.print_board_nums()

    letter = 'X' # Starting letter 
    # Iterate while the game still has empty square.
    # We don't have to worry about winner because we will just return that,
    # which breaks the loop. 
    while game.empty_squares():
        # Gets the move from the appropriate player. 
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # This function makes a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # An empty line 

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # After we made our move, we need to alternate letters.
            letter = 'O' if letter == 'X' else 'X' # Switches player
            
        # Tiny break for easier reading
        time.sleep(0.8)

    if print_game:
        print('It\s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomCompPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)