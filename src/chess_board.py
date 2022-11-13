from chess_piece import *
class PiecePlace:
        def init(self,row,col,piece=None):
            self.row=row 
            self.col=col
            self.piece=piece

        def has_piece(self):
            return self.piece !=None
class Board:
    def init(self):
        self.Piece_Arr = []
        for col in range(8):
          self.Piece_Arr.append([0, 0, 0, 0, 0, 0, 0, 0])
        self.draw_piece()
        self.add_pieces('white')
        self.add_pieces('black')

    def draw_piece(self):
        for row in range(8):
            for col in range(8):
               self.Piece_Arr[row][col]=PiecePlace(row,col)
    def add_pieces(self,color):
        if color=='white':
            first_row=6
            second_row=7
        else:
            first_row=1
            second_row=0

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