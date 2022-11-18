
from chess_piece import *
from chess_move import * 


class PiecePlace:
        def __init__(self,row,col,piece=None):
            '''
            this Constructor to run all time the piece and row and columnn for this square  
            '''
            self.row=row 
            self.col=col
            self.piece=piece # is object

        def has_piece(self):
            '''
            this method just to check if the square has a picec on it (true or false )
            '''
            return self.piece !=None
        def has_partners_piece(self, color):
            '''
            just to check if the squaer has a partners or not 
            '''
            return self.piece.color == color and self.has_piece()
        def enemies_piece(self,color):
            '''
            just to check if the squaer has an eneimes or not 
            '''
            #return self.piece.color != color and self.has_piece()
            return self.has_piece() and self.piece.color != color
        def empty_square(self):
            '''
            check if the squaer is empty or not 
            '''
            return self.piece==None
        def empty_or_enemies(self,color):
            '''
            check if the squaer is empty or has an eneime 
            '''
            return self.empty_square() or self.enemies_piece(color)
        
class Board:
    '''
    this class to add the pieces on the board  
    '''
    def __init__(self):

        self.Piece_Arr = []
        for col in range(8): # the for loob to create a 8 zeros for each columnn 
          self.Piece_Arr.append([0, 0, 0, 0, 0, 0, 0, 0])
        self.last_move=None
        self.draw_piece()
        self.add_pieces('white')
        self.add_pieces('black')
    def in_board(self ,*args):
        '''
        this method to chek  the range of the move 
        '''
        for arg in args:
            if arg<0 or arg>7:
                return False
        return True 
    
#______________ move method_________________#

    def move(self, piece, move, testing=False):
        "   mainما رح استخدم هاد الكود الي تحت كتبتو مباشره ب "
        "بس يخلص اخر واحد يحذفهم "
        # initial = move.initial
        # final = move.final
        # # console board move update
        # self.squares[initial.row][initial.col].piece = None
        # self.squares[final.row][final.col].piece = piece
        # # move
        # piece.moved = True

        # # clear valid moves
        # piece.clear_moves()  "مهم ما تتفعل "

        # # set last move
        # self.last_move = move


#_______________knight moves_________________#

    def knight_possible_move(self, pices ,row , column):
        '''
        this mthod to suggestion the possible move for the knight 
        '''
        knight_moves =[
                (row-2, column+1),
                (row-1, column+2),
                (row+1, column+2),
                (row+2, column+1),
                (row+2, column-1),
                (row+1, column-2),
                (row-1, column-2),
                (row-2, column-1),
            ]
        for knight_move in knight_moves :
            knight_move_row= knight_move[0]
            knight_move_column= knight_move[1]
            if self.in_board(knight_move_row,knight_move_column):
                if self.Piece_Arr[knight_move_row][knight_move_column].empty_or_enemies(pices.color):
                    start = PiecePlace(row , column)
                    end = PiecePlace(knight_move_row,knight_move_column)
                    move= Move(start,end)
                    pices.append_move(move)

    
    def king_moves(self, pices ,row , column):
            '''
            this mthod to suggestion the possible move for the King 
            '''
            adjs = [
                (row-1, column+0), 
                (row-1, column+1), 
                (row+0, column+1), 
                (row+1, column+1), 
                (row+1, column+0), 
                (row+1, column-1), 
                (row+0, column-1), 
                (row-1, column-1), 
            ]

            # normal moves
            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move

                if self.in_board(possible_move_row, possible_move_col):
                    if self.Piece_Arr[possible_move_row][possible_move_col].empty_or_enemies(pices.color):
                        # create squares of the new move
                        initial = PiecePlace(row, column)
                        final = PiecePlace(possible_move_row, possible_move_col) # piece=piece
                        # create new move
                        move = Move(initial, final)
                        pices.append_move(move)

            
#_______________pawn moves_________________#

    def pawn_possible_moves(self, piece ,row , column):

        # num. of steps valid
        if piece.moved:
            steps =1
        else:
            steps =2 # the pawn can move 2 steps if not move befor
        
        # the pown have to types of move:
        # 1. vertical move 

        pawn_start = row + piece.direction
        pawn_end = row + (piece.direction * (1+steps) )

        for possible_move_row in range(pawn_start, pawn_end, piece.direction):
            
            if self.in_board(possible_move_row):
                # we want to check if piece place is empty or rival 
                if self.Piece_Arr[possible_move_row][column].empty_square():
                     # 1. create initial and final move
                     # 2. create new move
                     # 3. append new move
                    initial_move = PiecePlace(row, column)
                    final_move = PiecePlace(possible_move_row,column)
                    move = Move(initial_move,final_move)

                    piece.append_move(move)

                else:
                    break  # because if the first square is not empty -> 
                           #we can't make possible the other place even though it's empty we arw already blocked
        # not in range
            else: 
                break 

        # 2. diagonal move (when eat piece) 
        # One step in diagonal then we don't need steps
        possible_move_row = row + piece.direction
        possible_move_cols = [column-1, column+1] # the value depend on the color

        for possible_move_col in possible_move_cols:
            if self.in_board(possible_move_row, possible_move_col):
                if self.Piece_Arr[possible_move_row][possible_move_col].enemies_piece(piece.color):
                    # if it has an enemy piece -> move right because we cannot move if diagonal is empty 
                    # or if it has a piece of the same color as ours so if it has an enemy piece ->can create a new move
                    # 1. create initial and final move
                    # 2. create new move
                    # 3. append new move

                    initial_move = PiecePlace(row, column)
                    final_move = PiecePlace(possible_move_row,possible_move_col)
                    move = Move(initial_move,final_move)

                    piece.append_move(move)


#_________________________________________
      
    def possible_moves(self, piece ,row , column):

        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = column + col_incr

                while True:
                    if self.in_board(possible_move_row, possible_move_col):
                        # create squares of the possible new move
                        initial = PiecePlace(row, column)
                        final_piece = self.Piece_Arr[possible_move_row][possible_move_col].piece
                        final = PiecePlace(possible_move_row, possible_move_col, final_piece)
                        # create a possible new move
                        move = Move(initial, final)

                        # empty = continue looping
                        if self.Piece_Arr[possible_move_row][possible_move_col].empty_square():
                           
                            piece.append_move(move)
                        

                        # has enemy piece = add move + break
                        elif self.Piece_Arr[possible_move_row][possible_move_col].enemies_piece(piece.color):
                            piece.append_move(move)
                            
                            break

                        # has team piece = break
                        elif self.Piece_Arr[possible_move_row][possible_move_col].has_partners_piece(piece.color):
                            
                            break
                    
                    # not in range
                    else: break

                    # incrementing incrs
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr
        '''
        this mthod to suggestion the possible move for the each pices when you need to move it 

        '''
        if piece.name == "knight":
            self.knight_possible_move( piece ,row , column)
        if piece.name == "pawn":
            self.pawn_possible_moves( piece ,row , column)
        if piece.name == "king":
            self.king_moves( piece ,row , column)
        if piece.name == "rook":
            
           straightline_moves([
              (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1), # left
           ])
        if piece.name == "bishop": 
            
           straightline_moves([
             (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
           ])
        if piece.name == "queen":
            straightline_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1) # left
            ])


    def draw_piece(self):
        '''
        this method  looping through for the 2D list to create instanse  (Reservation) for each square 
        the default value for the square is  no pieces on it  
        '''
        for row in range(8):
            for col in range(8):
               self.Piece_Arr[row][col]=PiecePlace(row,col)
    def add_pieces(self,color):
        '''
        this method to show the user the pices if user play in  white the pawns well be in row number 6
        and the other pieces well be in row number 7
        the other player well be the black which means the pawn well be the row number 1
        and the other pieces well be in 0 
        '''
        if color=='white':
            first_row=6
            second_row=7
        else:
            first_row=1
            second_row=0

        '''
         then create a new instance  for each pieces and put it in corect position 
        '''
        #Pawns
        for col in range (8):
            self.Piece_Arr[first_row][col]=PiecePlace(first_row,col,Pawn(color))
        # self.Piece_Arr[5][1]=PiecePlace(5,1,Pawn(color))
        # self.Piece_Arr[3][1]=PiecePlace(5,2,Pawn("white"))
        # self.Piece_Arr[first_row][col]=PiecePlace(first_row,col,Pawn(color))
        # rooks

        self.Piece_Arr[second_row][0] = PiecePlace(second_row, 0, Rook(color))
        self.Piece_Arr[second_row][7] = PiecePlace(second_row, 7, Rook(color))
        # self.Piece_Arr[5][5] = PiecePlace(5, 5, Rook("white"))
        # queen

        self.Piece_Arr[second_row][3] = PiecePlace(second_row, 3, Queen(color))
<<<<<<< HEAD
        # self.Piece_Arr[4][4] = PiecePlace(4, 4, Queen("white"))
=======
        # self.Piece_Arr[5][7] = PiecePlace(4, 4, Queen("white"))

>>>>>>> 9aeb363f9c7d9d954021b477308eb8f693704cc6
        # knights
        self.Piece_Arr[second_row][1] = PiecePlace(second_row, 1, Knight(color))
        self.Piece_Arr[second_row][6] = PiecePlace(second_row, 6, Knight(color))
        # self.Piece_Arr[3][3] = PiecePlace(3,3, Knight(color))
        # king
        self.Piece_Arr[second_row][4] = PiecePlace(second_row, 4, King(color))
<<<<<<< HEAD
        # self.Piece_Arr[5][3] = PiecePlace(5, 3, King(color))
=======
        # self.Piece_Arr[4][4] = PiecePlace(4, 4, King(color))
>>>>>>> 9aeb363f9c7d9d954021b477308eb8f693704cc6


        # bishops

        self.Piece_Arr[second_row][2] = PiecePlace(second_row, 2, Bishop(color))
        self.Piece_Arr[second_row][5] = PiecePlace(second_row, 5, Bishop(color))
        # self.Piece_Arr[4][7] = PiecePlace(4, 7, Bishop(color))




if __name__ =="__main__":

    board=Board()
    print(board.Piece_Arr[0][0]. has_piece())
    print(board.Piece_Arr[5][5]. has_piece())
    print(board.Piece_Arr[0][0].piece.image)
    print(board.Piece_Arr[7][1].piece.image)
    print(board.Piece_Arr[7][1].piece.color)
    print(board.Piece_Arr[0][1].piece.color)
    print(board.Piece_Arr[0][4].piece.name)
    print(board.Piece_Arr[1][5].piece.name)