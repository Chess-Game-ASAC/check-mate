import pygame

from chess_game import Game 

class Main:

  def __init__(self):
    # to initialize pygame library
    pygame.init()
    self.screen = pygame.display.set_mode( (600,600) )
    pygame.display.set_caption('Check Mate')
    self.game=Game()
    
  def mainloop(self):
    
    while True:
      self.game.show_bg(self.screen)
      self.game.show_pieces(self.screen)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()

      
      pygame.display.update() #should be the last line in the code to update the board

main=Main()
main.mainloop()

