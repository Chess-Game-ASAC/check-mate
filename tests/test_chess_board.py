from chess_board import *


# check the board have pecie in a specific place
def test_check_the_board_have_pieces1():
    board=Board()
    assert board.Piece_Arr[0][0]. has_piece()==True 

def test_check_the_board_have_pieces2():
    board=Board()
    assert board.Piece_Arr[5][5]. has_piece()==False 

# check the piece in_correct_place in chess board
def test_check_the_Rook_in_correct_place():
    board=Board()
    assert board.Piece_Arr[0][0].piece.image=="images/imgs-80px/black_rook.png"


def test_check_the_knights_in_correct_place():
    board=Board()
    assert board.Piece_Arr[7][1].piece.image=="images/imgs-80px/white_knight.png"


# check the color of piece in a specific place
def test_check_the_pieceColor_in_selected_place1():
    board=Board()
    assert board.Piece_Arr[7][1].piece.color=="white"

def test_check_the_pieceColor_in_selected_place2():
    board=Board()
    assert board.Piece_Arr[0][1].piece.color=="black"

# check the name of piece in a specific place
def test_check_the_pieceName_in_selected_place1():
    board=Board()
    assert board.Piece_Arr[6][1].piece.name=="pawn"

def test_check_the_pieceName_in_selected_place2():
    board=Board()
    assert board.Piece_Arr[7][7].piece.name=="rook"
def test_check_the_pieceName_in_selected_place3():
    board=Board()
    assert board.Piece_Arr[0][3].piece.name=="queen"

def test_check_the_pieceName_in_selected_place4():
    board=Board()
    assert board.Piece_Arr[1][5].piece.name=="pawn"

def test_check_the_pieceName_in_selected_place5():
    board=Board()
    assert board.Piece_Arr[0][4].piece.name=="king"