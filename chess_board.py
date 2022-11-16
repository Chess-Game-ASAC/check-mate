
from chess_piece import *
from chess_move import * 


class PiecePlace:
        def __init__(self,row,col,piece=None):
            '''
            this Constructor to run all time the piece and row and column for this square  
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
            return self.piece.color != color and self.has_piece()
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
        for col in range(8): # the for loob to create a 8 zeros for each column 
          self.Piece_Arr.append([0, 0, 0, 0, 0, 0, 0, 0])
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
    def knight_possible_move(self, pices ,row , colum):
        '''
        this mthod to suggestion the possible move for the knight 
        '''
        knight_moves =[
                (row-2, colum+1),
                (row-1, colum+2),
                (row+1, colum+2),
                (row+2, colum+1),
                (row+2, colum-1),
                (row+1, colum-2),
                (row-1, colum-2),
                (row-2, colum-1),
            ]
        for knight_move in knight_moves :
            knight_move_row= knight_move[0]
            knight_move_colum= knight_move[1]
            if self.in_board(knight_move_row,knight_move_colum):
                if self.Piece_Arr[knight_move_row][knight_move_colum].empty_or_enemies(pices.color):
                    start = PiecePlace(row , colum)
                    end = PiecePlace(knight_move_row,knight_move_colum)
                    move= Move(start,end)
                    pices.append_move(move)


    def possible_moves(self, pices ,row , colum):
        '''
        this mthod to suggestion the possible move for the each pices when you need to move it 

        '''
        if pices.name == "knight":
            self.knight_possible_move( pices ,row , colum)
        if pices.name == "pawn":
            pass
        if pices.name == "king":
            pass
        if pices.name == "rook":
            pass
        if pices.name == "queen":
            pass
        if pices.name == "bishop":
            pass

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

        # rooks
        self.Piece_Arr[second_row][0] = PiecePlace(second_row, 0, Rook(color))
        self.Piece_Arr[second_row][7] = PiecePlace(second_row, 7, Rook(color))

        # queen
        self.Piece_Arr[second_row][3] = PiecePlace(second_row, 3, Queen(color))

        # knights
        self.Piece_Arr[second_row][1] = PiecePlace(second_row, 1, Knight(color))
        self.Piece_Arr[second_row][6] = PiecePlace(second_row, 6, Knight(color))
        # king
        self.Piece_Arr[second_row][4] = PiecePlace(second_row, 4, King(color))

        # bishops
        self.Piece_Arr[second_row][2] = PiecePlace(second_row, 2, Bishop(color))
        self.Piece_Arr[second_row][5] = PiecePlace(second_row, 5, Bishop(color))




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