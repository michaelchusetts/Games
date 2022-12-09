"""
Tic - Tac - Toe
11-29-22 - Michael Newman

V1.0 with all normal rules included, vertical, horizontal, & diagnol win conditions including no winner. 
checks every move to make sure each one is valid.
asks if you want to play again after game over

would like to add:
    replay with same players
    timer & better gui 
    support for larger grids while still maintaining the same ruleset (ie 3 in a row still wins)
    predictability when game is over before 9 turns
    online mode for facing random oponents 
    effects
"""

from getkey import getkey, key
import string

class player():
    def __init__(self, name, symbol) -> None:
        self.name = name
        self.symbol = symbol
    def __str__(self) -> str:
        return '%s is playing as %s' % (self.name, self.symbol)
        
class board():
    def __init__(self, x, y, ) -> None:
        self.width = x
        self.height = y
        self.board = []
        self.char_board = list(string.ascii_uppercase[:self.width])
        self.game_over = False
        #this loops creates the grid based off the given height and width
        for i in range(0, self.height):
            self.board.append(list(self.width * ' '))

    def __str__(self) -> str:
        return self.board

    def print_board(self) -> None:
        #draws the board with labels 
        print(' ', self.char_board)
        for i in range(len(self.board)):
            print(i+1, self.board[i]) 
    
    def make_move(self, player, x, y) -> None:
        #this 'draws' the moving pieces on the board
        self.board[x-1][self.char_board.index(y.upper())] = player.symbol
        self.print_board()

    def validate_move(self, player, x, y) -> bool:
        if x.isnumeric() and y.isalpha():
            #change inputs to match conditionals 
            x=int(x)
            y=y.upper()
            if x > len(self.board[0]):
                #x is out of range horizontaly
                return False

            elif y not in self.char_board:
                #y is out of range vertically
                return False

            if self.board[x-1][self.char_board.index(y)] == ' ':
                #only valid space
                print('\n')
                self.make_move(player, x, y)
                return True

            elif self.board[x-1][self.char_board.index(y)] == player.symbol:
                #space is already taken
                return False

            else:
                #space is already taken
                return False
        else:
            # if x & y aren't the right types
            return False

    def check_win(self, p1, p2) -> bool:
        p1win = list(self.width * p1.symbol)
        p2win = list(self.width * p2.symbol)
        br = range(0, self.height)
        #diagonal win  -- top left to bottom right
        if [self.board[i][i] for i in br] == p1win or [self.board[i][i] for i in br] == p2win:
            return True

        #diagonal win  -- bottom left to top right  >_<
        if [self.board[2][0], self.board[1][1], self.board[0][2]] == p1win or [self.board[2][0], self.board[1][1], self.board[0][2]] == p2win:
            return True

        #vertical win  -- 1st colom, 2nd..3rd
        for y in br:
            if [self.board[i][y] for i in br] == p1win or [self.board[i][y] for i in br] == p2win:
                return True

        #horizontal win -- 1st row, 2nd..3rd
        for h in self.board:
            if h == p1win or h == p2win:
                return True
        return False

def play(replay=None, p1=None, p2=None):
    if replay:
        print("Play again?")
        print('\n')

    print('Press Enter to begin or Esc to exit\n'.title())
    choice = getkey()
    if choice == key.ENTER:
        print('let the games begin'.title())
        print('\n')
        main(replay, p1, p2)
    if choice == key.ESCAPE:
        print('Bye Bye!')
        quit()

# main game loop after starting game
def main(replay, p1, p2):      
    if replay != True:
        print("Enter player 1's name...")
        p1name = input()
        print("Enter player 1's symbol...")
        while True:
            p1sym = input()
            if 0< len(p1sym) <2:
                break
            else:
                print('One letter only!')
        print("Enter player 2's name...")
        p2name = input()
        print("Enter player 2's symbol...")
        while True:
            p2sym = input()
            if 0< len(p2sym) <2:
                break
            else:
                print('One letter only!')
        player1 = player(p1name, p1sym)
        player2 = player(p2name, p2sym)
    else:
        player1 = p1
        player2 = p2

    print('\n')
    print(player1)
    print(player2)
    print('\n')
    game_board = board(3, 3)
    game_board.print_board()
    print('\n')
    turn = player1
    turn_count = 1

    while game_board.game_over != True:
        #   get move from current players turn
        print("%s's turn to make a move..." % (turn.name.title()))
        #   make sure playe one makes a valid move
        while True:
            print('\n')
            if game_board.validate_move(turn, input("Row...\n"), input("Colom...\n")) != True:
                print('\n')
                print('Invalid move')
                print('Try Again')
                print('\n')
                game_board.print_board()
            else:
                print('\n')
                break
        
        #check if someone won
        if game_board.check_win(player1, player2):
            print("%s wins on turn %s" % (turn.name.title(), turn_count))
            break
        else:
            turn_count += 1
            #switch turns
            if turn == player1:
                turn = player2
            else:
                turn = player1
        if turn_count > 9:
            print('No winner')
            break       
    play(True, player1, player2)

print('tic-tac-toe'.title())
play()