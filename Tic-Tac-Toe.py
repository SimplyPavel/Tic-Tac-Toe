import sys
import random

class Build_board():
    boardg = []
    num_of_rows, num_of_cols = 3, 3
    
    def generate(self):
        self.boardg[:] = []
        for x in range(self.num_of_rows):
            self.boardg.append(['0'] * self.num_of_cols)

    def print_board(self):
        for row in self.boardg:
            print(" ".join(row))

class Players(object):
    name = ""
    score = 0
    players_dic = {}
    def ask_name(self):
        for i in range(2):
            while True:
                self.name = input("What's {plyr} player's name? \n".format(plyr="first" if i == 0 else "second"))
                if self.name.isalpha() == False:
                    continue
                else:
                    break
            self.players_dic["p" + str(i+1) + "_name"] = self.name
            self.players_dic["p" + str(i+1) + "_score"] = self.score

class Players_turn(Players):
    def __init__(self, turn):
        self.turn = turn

    def whos_turn(self):
        if self.turn % 2 == 1:
            return self.players_dic['p1_name'], '1'
        elif self.turn % 2 == 0:
            return self.players_dic['p2_name'], '2'
        else:
            return '3', '3'

# Exceptions -Open Section
class PlayAgain(Exception):
    pass

class TooHighIndex(Exception):
    pass
    
class OccupiedSquare(Exception):
    pass

class Cheat(Exception):
    pass
# Exceptions -Close Section

if __name__ == '__main__':

    board, players = Build_board(), Players()

    players.ask_name()
    pdic = players.players_dic

    turn = 0
    players_turn = Players_turn(turn)

    def check_if_win():
        tp = tuple(zip(*board.boardg))
        if tuple('1' * 3) in tp or (['1']*len(board.boardg[0]) in board.boardg):
            pdic['p1_score'] += 1
            print('Players 1 wins this round!')
            print(pdic['p1_name'], ':', pdic['p1_score'], '\n' + pdic['p2_name'], ':', pdic['p2_score'])
            return 1
        elif tuple('2' * 3) in tp or (['2']*len(board.boardg[0]) in board.boardg):
            pdic['p2_score'] += 1
            print('Players 2 wins this round!')
            print(pdic['p1_name'], ':', pdic['p1_score'], '\n' + pdic['p2_name'], ':', pdic['p2_score'])
            return 1
        else: 
            return 0

    def cheat_tie(lst):
        for i, item in enumerate(lst):
            if isinstance(item, list):
                alter_elements(item)
            else:
                x = random.randint(1, 2)
                lst[i] = str(x)
        if check_if_win() == 1:
            alter_elements(lst)

    def hit():
        while True:
            try:
                where_row, where_col = int(input("Which row: ")) - 1, int(input("Which col: ")) - 1
                if where_row == 122 and where_col == 122:
                    print('cheat on')
                    cheat_tie(board.boardg)
                elif where_row > 3 or where_col > 3:
                    raise TooHighIndex
                elif board.boardg[where_row][where_col] != '0':
                    raise OccupiedSquare
                else:
                    board.boardg[where_row][where_col] = players_turn.whos_turn()[1]
            except ValueError:
                print('Sorry, numbers only!')
            except TooHighIndex:
                print('One or two numbers are too high. Up to 3.')
            except OccupiedSquare:
                print('Choose another square.')
            else:
                break    
    
    def game():
        for round in range(1):
            print("\nRound:", round + 1, "\n")
            board.generate()
            turn = 0
            while True: 
                turn += 1
                players_turn.turn = turn
                print("Turn:", turn)
                if any('0' in list_ for list_ in board.boardg):
                    print("It's", players_turn.whos_turn()[0] + "'s turn.") 
                    board.print_board()
                    print("")
                    hit()
                    if check_if_win() > 0:
                        break
                else:
                    print('Sorry. It\'s a tie.')
                    break  
        while True:
            try:
                q = str(input("Would you like to play again? y/n"))
                if q == 'y':
                    raise PlayAgain
            except ValueError:
                "Only 'y' or 'n'."
                continue
            except PlayAgain:
                game()
            else:
                break
        sys.exit()

    game()
