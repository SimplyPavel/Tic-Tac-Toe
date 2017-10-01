import sys


class Build_board():
    boardg = []
    num_of_rows = 3
    num_of_cols = 3
    def generate(self):
        for x in range(self.num_of_rows):
            self.boardg.append(['0' for x in range(self.num_of_cols)])

    def print_board(self):
        for row in self.boardg:
            print(" ".join(row))

class Players(object):
    name = ""
    score = 0
    players_dic = {}
    def ask_name(self):
        for i in range(2):
            self.name = input("What's {plyr} player's name? ".format(plyr="first" if i == 0 else "second"))
            self.players_dic["p" + str(i+1) + "_name"] = self.name
            self.players_dic["p" + str(i+1) + "_score"] = self.score

 
class Players_turn(Players): #PROBLEM HERE

    def __init__(self, turn):
        self.turn = turn

    def whos_turn(self):
        if self.turn == 1:
            return self.players_dic['p1_name'], '1'
        elif self.turn == 2:
            return self.players_dic['p2_name'], '2'
        else:
            return 'incorrect', '3'



if __name__ == '__main__':

    turn = 0

    board = Build_board()
    board.generate()

    players = Players()
    players.ask_name()
    pdic = players.players_dic

    players_turn = Players_turn(turn)
    who_now = players_turn.whos_turn()

    def check_if_win():
    #   for i in range(len(board.boardg[0])):
    #        board.boardg[2][i] = '1'
        #for i in range(len(board.boardg)):
            #board.boardg[i][0] = '1'
        tp = tuple(zip(*board.boardg))
        if tuple('1' * 3) in tp or (['1']*len(board.boardg[0]) in board.boardg):
            pdic['p1_score'] += 1
            print('Players 1 wins!')
            print(pdic['p1_name'], ':', pdic['p1_score'])
            print(pdic['p2_name'], ':', pdic['p2_score'])
            return False
        elif tuple('2' * 3) in tp or (['2']*len(board.boardg[0]) in board.boardg):
            pdic['p2_score'] += 1
            print('Players 2 wins!')
            print(pdic['p1_name'], ':', pdic['p1_score'])
            print(pdic['p2_name'], ':', pdic['p2_score'])
            return False
        else: 
            return True



    def hit():
        where_row = int(input("Which row: ")) - 1
        where_col = int(input("Which col: ")) - 1
        if board.boardg[where_row][where_col] == '0':
            board.boardg[where_row][where_col] = who_now[1]
        else:
            print('Choose another square.')
            hit()


    def game():
        for round in range(3):
            while True:
                global turn #PROBLEM HERE
                turn += 1 #PROBLEM HERE
                players_turn = Players_turn(turn) #PROBLEM HERE
                print("Turn", turn)
                if ['0' in list_ for list_ in board.boardg]:
                    print("It's", players_turn.whos_turn()[0] + "'s turn.") #PROBLEM HERE
                    board.print_board()
                    hit()
                    check_if_win()
                else:
                    print('Sorry. It\'s a tie.')
                    return False
        sys.exit()

game()
               
