import pygame
import sys

from constant_info import *

class Main:

  def __init__(self):
    # to initialize pygame library
    pygame.init()
    self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
    pygame.display.set_caption('Chess')
    
  def mainloop(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

      
      pygame.display.update() #should be the last line in the code to update the board

main=Main()
main.mainloop()

