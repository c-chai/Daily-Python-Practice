import random
import re # For regex module, used for splitting strings based on specific patterns 

class Board:
    '''
    This class is the blueprint for the board! 
    '''
    def __init__(self, dim_size, num_bombs):
        '''
        This method is automatically called when a new Board is created.
        It sets up the board with dimensions (dim_size) and number of bombs (num_bombs).
        '''
        self.dim_size = dim_size
        self.num_bombs = num_bombs    
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        '''
        This function creates a new board as a list of lists (most natural way) because this is 2D.
        '''
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            # This loop randomly places bombs ('*') on the board until the total number of bombs (num_bombs) is reached. 
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size 
            if board[row][col] == '*':
                continue
            board[row][col] = '*' 
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        '''
        This function goes through each cell on the board, and if it's not a bomb, assigns a number
        representing how many neighboring cells contain bombs. 
        '''
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        '''
        This function calculates the number of bombs adjacent to a given cell (specified by 'row' and 'col').
        '''
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size, row+2)):
            for c in range(max(0, col-1), min(self.dim_size, col+2)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, col):
        '''
        This function represents the specific action of digging a cell. 
        If cell is a 0 (no neighboring bombs), recursively uncovers neighboring cells. 
        Returns False if a bomb is dug (GAME OVER).
        '''
        self.dug.add((row, col))
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        for r in range(max(0, row-1), min(self.dim_size, row+2)):
            for c in range(max(0, col-1), min(self.dim_size, col+2)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        return True

    def __str__(self):
        '''
        This function returns a string representation of the board. 
        It is a magic function which returns a human-readable string of an object! 
        '''
        visible_board = [[' ' for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
        return "\n".join([" ".join(row) for row in visible_board])

def play(dim_size=10, num_bombs=10):
    '''
    This function sets up and runs the game. 
    It creates a board and allows user to choose cells to dig until they hit a bomb or clear the board. 
    '''
    board = Board(dim_size, num_bombs)
    safe = True 
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        '''
        This loop continues as long as the number of dug cells is < (total cells - number of bombs)
        This checks for game over conditions as user inputs their dig location. 
        '''
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row, col: ")) # This gets the user's input, splits it into row and column values, and makes sure they are valid. 
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size: 
            print("Invalid location. Try again.")
            continue
        safe = board.dig(row, col)
        if not safe:
            break
    
    if safe:
        print("Congratulations!! YOU WON")
    else:
        print("Sorry GAME OVER")
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

# Code block below runs the 'play' function, starting the game, only if the script is the main program being executed (not imported as a module).
if __name__ == '__main__':
    play()
