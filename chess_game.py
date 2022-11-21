import pygame
from chess_board import Board
from motion import Motion
from settings import*
from config import Config
    
class Game:

    ''' the game class response to rendering method'''

    def __init__(self):
        self.board=Board()
        self.motion=Motion()
        self.next_player="white"
        self.config = Config()


    def show_background(self ,surface):

        '''the function to draw the board'''
        theme = self.config.theme

        for row in range(8):

            for col in range(8):
                color = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
                rect = (col*75,row*75,75,75) # tuple (x,y,W,H)
                pygame.draw.rect(surface,color,rect)


    def show_pieces(self,surface):

        for row in range(8):
          for col in range(8):
            #check if the square have piece then show the piece on the chess board in the center of his square
            if self.board.Piece_Arr[row][col].has_piece():
                
                piece=self.board.Piece_Arr[row][col].piece  # saving that piece into a variable

                if piece is not self.motion.piece:
                   # print("11111",piece)
                   img = pygame.image.load(piece.image)
                   # print("2222222",img)
                   img_center = col * 75 + 75 // 2, row * 75 + 75 // 2
                   # print("333333333",img_center)
                   piece.image_rect = img.get_rect(center=img_center)
                   # get_rect -> this is pygame method
                   # print("4444444",piece.image_rect)
                   # blit() is function in pygame to draw one image into another
                   surface.blit(img, piece.image_rect)
    
    def show_possible_move(self, surface):
        '''
        this method to show the possible move for each pieces 
        '''
        theme = self.config.theme

        if self.motion.moving :
            piece = self.motion.piece
    #   "#e9ed11" 
            # loop all valid moves
            for move in piece.moves:
                # color
                color = theme.moves.light if (move.end.row + move.end.col) % 2 == 0 else theme.moves.dark                  
               
                # rect
                rect = (move.end.col * 75, move.end.row * 75, 75, 75)
                # blit
                pygame.draw.rect(surface, color, rect)
    
    def next_turn(self):
        if self.next_player=="white":
            self.next_player="black" 
        else:
            self.next_player="white"

    def show_last_move(self,surface):
        theme = self.config.theme
        if self.board.last_move is not None:
            #color the start square
            strat_move=self.board.last_move.start
            color = theme.trace.light
            rect = (strat_move.col * 75, strat_move.row * 75, 75, 75)
            pygame.draw.rect(surface, color, rect)
          #color the start square
            end_move=self.board.last_move.end
            theme.trace.dark
            rect = (end_move.col * 75, end_move.row * 75, 75, 75)
            pygame.draw.rect(surface, color, rect) # part of square ,width=6

    def change_theme(self):
        
        self.config.change_theme()

    def reset(self):
        self.__init__()
    
    