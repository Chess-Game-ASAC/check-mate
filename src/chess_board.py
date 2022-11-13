from chess_piece import *
class PiecePlace:
        def __init__(self,row,col,piece=None):
            '''
            this Constructor to run all time the piece and row and column for this square  
            '''
            self.row=row 
            self.col=col
            self.piece=piece

        def has_piece(self):
            '''
            this method just to check if the square has a picec on it (true or false )
            '''
            return self.piece !=None
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