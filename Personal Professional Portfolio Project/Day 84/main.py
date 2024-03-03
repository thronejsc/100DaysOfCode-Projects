from random import randint, choice

class Board:
    def __init__(self):
        self.columns = 3
        self.tile = ['-']
        self.column_numbers = [f"{i+1}" for i in range(self.columns)]
        self.board = [self.tile * 3 for i in range(self.columns)]
        self.game_is_finished = False
        self.display_board()
    
    def display_board(self):
        print("    " + "    ".join(self.column_numbers))
        for rows in range(len(self.board)):
            if rows == 0:
                print(f"{rows + 1} {self.board[rows]}")
            else:
                print(f"\n{rows + 1} {self.board[rows]}")
                
    def player_turn(self):
        print("\nPlayer's Turn")
        row_tile = int(input("\ninput row: "))
        column_tile = int(input("\ninput column: "))
    
        if row_tile == 0 and column_tile == 0:
            self.game_is_finished = True
        board.board[row_tile - 1][column_tile - 1] = "X"
        self.display_board()
        self.check_if_win()
        
    
    def computer_turn(self):
        print("\nComputer's Turn")
        random_row = randint(0,2)
        random_column = randint(0,2)
        self.computer_choice = (random_row,random_column)
        if self.check_if_occupied():
            if "-" not in self.board:
                self.game_is_finished = True
                print("No more tiles to fill")
            else:
                self.computer_turn()
        else:
            board.board[self.computer_choice[0]][self.computer_choice[1]] = "O"
            self.display_board()
            self.check_if_win()
            
    
    def check_if_occupied(self):
        if board.board[self.computer_choice[0]][self.computer_choice[1]] != "-":
            return True
    
    
    def check_if_win(self):
        # check if there are same values in a row
        for row in self.board:
            all_row_x = all(tile == 'X' for tile in row )
            all_row_o = all(tile == 'O' for tile in row )
            
            
            straight_diag1 = (self.board[0][0], self.board[1][1], self.board[2][2])
            straight_diag2 = (self.board[2][0], self.board[1][1], self.board[0][2])
            all_diag_o = all(i == 'O' for i in straight_diag1)  or  all(i == 'O' for i in straight_diag2)
            all_diag_x = all(i == 'X' for i in straight_diag1)  or  all(i == 'X' for i in straight_diag2)

            if all_row_x or all_row_o or all_diag_o or all_diag_x:
                if all_row_o or all_diag_o:
                    print("The winner is O")
                    self.game_is_finished = True
                elif all_row_x or all_diag_x:
                    print("The winner is X")
                    self.game_is_finished = True
                
        

# columns = 3
# tile = ['-']
# column_numbers = [f"{i+1}" for i in range(columns)]
# board = [tile * 3 for i in range(columns)]

board = Board()


while not board.game_is_finished:
    board.player_turn()
    board.computer_turn()
    
    
    
    
    
