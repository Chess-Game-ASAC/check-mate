import pygame
from chess_game import Game 


class Main:
  """
  Overall class to manage game assets and behavior.
  """

  def __init__(self):
    """ Initialize the game, and create resources. """
    pygame.init()     # to initialize pygame library
    self.screen = pygame.display.set_mode( (600,600) )     #create screen attribute
    pygame.display.set_caption('Check Mate')     # add the title of the screen
    self.game=Game()
    
  def mainloop(self):
    """
    Start the main loop for the game.
    1. check if any event happen 
    2. update the secreen 
    
    """
    while True:
      self.game.show_bg(self.screen)
      self.game.show_pieces(self.screen)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()

      pygame.display.update()   #should be the last line in the code to update the board

main=Main()
main.mainloop()

