#test the chess pecies file 
from chess_piece import *
import pytest
#test the white pecies
def test_King():
    king=King( "white")
    assert king.image=="images/imgs-80px/white_king.png"
def test_Queen():
    queen=Queen( "white")
    assert queen.image=="images/imgs-80px/white_queen.png"
def test_knight():
    knight=Knight( "white")
    assert knight.image=="images/imgs-80px/white_knight.png"

def test_Bishop():
    bishop=Bishop( "white")
    assert bishop.image=="images/imgs-80px/white_bishop.png"
def test_Rook():
    rook=Rook( "white")
    assert rook.image=="images/imgs-80px/white_rook.png"
def test_Pawn():
    pawn=Pawn( "white")
    assert pawn.image=="images/imgs-80px/white_pawn.png"

# test the black pecies
def test_King_black():
    king=King( "black")
    assert king.image=="images/imgs-80px/black_king.png"
def test_Queen_black():
    queen=Queen( "black")
    assert queen.image=="images/imgs-80px/black_queen.png"
def test_knight_black():
    knight=Knight( "black")
    assert knight.image=="images/imgs-80px/black_knight.png"

def test_Bishop_black():
    bishop=Bishop( "black")
    assert bishop.image=="images/imgs-80px/black_bishop.png"
def test_Rook_black():
    rook=Rook( "black")
    assert rook.image=="images/imgs-80px/black_rook.png"
def test_Pawn_black():
    pawn=Pawn( "black")
    assert pawn.image=="images/imgs-80px/black_pawn.png"