# A human or computer can play in this program 
import math
import random 

class Player:
    def __init__(self, letter):
        # Letter is x or o
        self.letter = letter 

    # We want all players to get their next move given a game 
        def get_move(self, game):
            pass
    
class RandomCompPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):' ) 
            '''
            To check that this is a correct value, we will try to cast it to an integer, 
            and if it is not, we say it's invalid.
            If that spot is unavailable on the board, we will also say it's invvalid. 
            '''
            try: 
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again')
        
        return val