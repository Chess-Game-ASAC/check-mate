import pygame
from chess_board import Board


    
class Game:

    ''' the game class response to rendering method'''

    def __init__(self):
        self.board=Board()
        


    def show_background(self ,surface):

        '''the function to draw the board'''

        for row in range(8):

            for col in range(8):

                if (row+col)%2==0:
                    color = (230, 186, 149) 
                else :
                    color = (251, 250, 205) 
                
                rect = (col*75,row*75,75,75) # tuple (x,y,W,H)
                pygame.draw.rect(surface,color,rect)


    def show_pieces(self,surface):

        for row in range(8):
          for col in range(8):
            #check if the square have piece then show the piece on the chess board in the center of his square
            if self.board.Piece_Arr[row][col].has_piece():
                piece=self.board.Piece_Arr[row][col].piece
                # print("11111",piece)
                img = pygame.image.load(piece.image)
                # print("2222222",img)
                img_center = col * 75 + 75 // 2, row * 75 + 75 // 2
                # print("333333333",img_center)
                piece.image_rect = img.get_rect(center=img_center)
                # print("4444444",piece.image_rect)
                # blit() is function in pygame to draw one image into another
                surface.blit(img, piece.image_rect)
