from chess_game import *
from motion import Motion
from chess_piece import *

import pytest

@pytest.fixture
def motion ():
    motion=Motion()
    col,row=(260, 500)
    motion.MouseMotion(col,row)
    motion.update(row//75,col//75) 
    return motion


def test_MouseMotion_methode(motion):
    assert motion.M_row ==500 and motion.M_col==260

def test_update_methode(motion):
    assert motion.col_y==260//75 and motion.row_x==500//75

@pytest.fixture
def game ():
    game=Game()
    motion=game.motion
    board=game.board
    col,row=(260, 500)
    motion.MouseMotion(col,row)
    motion.update(row//75,col//75) 
    motion.save_piece(board.Piece_Arr[row//75][col//75].piece)

    return game

# test in game .motion
def test_MouseMotion_methode2(game):
    assert game.motion.M_row ==500 and game.motion.M_col==260

def test_update_methode2(game):
    assert game.motion.col_y==260//75 and game.motion.row_x==500//75

def test_save_piece_motion(game):
    assert game.motion.piece.name=="pawn"
def test_save_piece_motion2(game):
    assert game.motion.piece.color=="white"

def test_motion_delete_piece(game):
    game.motion.delete_piece()
    assert game.motion.piece==None and game.motion.M_row==None and game.motion.M_col==None and game.motion.moving== False

#test in game .board
def test_board_Piece_Arr(game):
    assert game.board.Piece_Arr[500//75][260//75].has_piece()== True

