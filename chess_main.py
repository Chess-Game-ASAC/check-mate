import pygame
import sys  # this model is help to quit the application
from chess_game import Game 
from chess_move import Move


class Main:
  """
  Overall class to manage game assets and behavior.
  """

  def __init__(self):
    """ Initialize the game, and create resources. """

    pygame.init()     # to initialize pygame library
    self.screen = pygame.display.set_mode( (600,600) )     #create screen attribute (width,hight)
    
    pygame.display.set_caption('Check Mate')     # add the title of the screen
    self.game=Game() 
    
  def mainloop(self):
    """
    Start the main loop for the game.
    1. check if any event happen 
    2. update the secreen 
    3. responsible of calling all other classes
    
    """
    game = self.game
    motion=self.game.motion  
    board=self.game.board
    
    while True:
      motion=self.game.motion  #call the motion attribute in the game class which is object "Motion class"
      board=self.game.board  #call the board attribute in the game class which is object "Board class"
      
      self.game.show_background(self.screen)  #display the board
      self.game.show_last_move(self.screen)
      self.game.show_possible_move(self.screen)
      self.game.show_pieces(self.screen) #put the pieces on the board
      
      if motion.piece is not None and motion.M_col is not None and motion.M_row is not None:
        motion.update_screen(self.screen)


      for event in pygame.event.get():   #loop through the event
        # we have three events
        # 1. click event to select the piece need to move 
        if event.type ==pygame.MOUSEBUTTONDOWN:
          col,row=event.pos
          motion.MouseMotion(col,row)
          col=col//75
          row=row//75
          motion.update(row,col) 

          if board.Piece_Arr[row][col].has_piece():
            #check if it the valid piece (color) 
            if self.game.next_player==board.Piece_Arr[row][col].piece.color:
              board.possible_moves(board.Piece_Arr[row][col].piece,row,col)
              motion.save_piece(board.Piece_Arr[row][col].piece)
              self.game.show_background(self.screen)
              self.game.show_last_move(self.screen)
              self.game.show_possible_move(self.screen)
              self.game.show_pieces(self.screen)
              

        # 2. mouse motion event to move the piece in specifiic square 
        elif event.type ==pygame.MOUSEMOTION:
          col,row=event.pos
          # motion.new_postion(row,col)
          if motion.piece is not None:
            motion.MouseMotion(col,row)
            self.game.show_background(self.screen)  
            self.game.show_last_move(self.screen)
            self.game.show_possible_move(self.screen)
            self.game.show_pieces(self.screen) 
            motion.update_screen(self.screen)
           

        # 3. releasing your click event 
        elif event.type == pygame.MOUSEBUTTONUP:
          col,row=event.pos
          col=col//75
          row=row//75
          if motion.moving :   # check if have moving 
            piece = motion.piece  #self.game.motion.piece 
            # loop all valid moves and heck if select move in the valid move 
            for move in piece.moves:
    
              if move.end.row==row and move.end.col==col :
                  #delete the previse row and col  
                  board.Piece_Arr[motion.row_x][motion.col_y].piece=None
                  board.Piece_Arr[row][col].piece=motion.piece  #the final row and col have piece
                  piece.moved=True   # this pieces moved
                  board.last_move=move   # to change the square color of the last move 
                  #next turn
                  self.game.next_turn() 
                  board.move(motion.piece, move)  
                  self.game.show_background(self.screen)  
                  self.game.show_last_move(self.screen)
                  self.game.show_pieces(self.screen) 
                  break
                   
            piece.moves=[]      

          motion.delete_piece()

        #4. restart the game  
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
              game.reset()
              game = self.game
              motion=self.game.motion  
              board=self.game.board
        # 4. quite the check mate game  
        elif event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()


      pygame.display.update()   #should be the last line in the code to update the board

main=Main()
main.mainloop()