import pygame
from Menu_System import MainMenu , Menu,rulesMenu,CreditsMenu
from chess_main import *
from chess_main import Main

class GameW():
    def __init__(self):
        pygame.init()  # init give us access to all feature in pygame
        self.main=None
        self.running = True  # true when the game is on
        self.playing = False

        # these var. for controls , to iterate throgh the menu , when player presses the up key this var. shold be set the true
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

        # canvas square dimention
        self.DISPLAY_W = 700
        self.DISPLAY_H = 700
        
        # create canvas 
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        
        # create a window 
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        
        # tell python the path of font file, I put it in the same place of game file
        self.font_name = '8-BIT WONDER.TTF'

        # if you want use the default font
        self.font_named = pygame.font.get_default_font() 

        # self.BLACK = (241, 211, 179)
        # self.WHITE = (139, 126, 116)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.main_menu = MainMenu(self) #the game it pass itself as parameter in MainMenu
        self.rules = rulesMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):

            while self.playing:
                self.check_events()

                if self.START_KEY:
                    self.playing= False

                self.display.fill(self.BLACK)
                self.main=Main()
                self.main.mainloop()
                
                # self.window.blit(self.display, (0,0))
                # pygame.display.update()
                # self.reset_keys()
                # self.draw_text('Thanks for Playing Check Mate', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
               




                # we flio to the next page by resetting our screen by filling it black



        # check the player inputs & see what buttons they are pressing
    def check_events(self):
            for event in pygame.event.get():

                if event.type == pygame.QUIT:  # check if the player has clicked the x at the top of the window
                    self.running, self.playing = False, False  # to break the game cycle
                    self.curr_menu.run_display = False
                
                # if the player press anything on the keyboard
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.START_KEY = True
                    if event.key == pygame.K_BACKSPACE:
                        self.BACK_KEY = True
                    if event.key == pygame.K_DOWN:
                        self.DOWN_KEY = True
                    if event.key == pygame.K_UP:
                        self.UP_KEY = True

        # we need reset these variables 
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y,color= (255, 255, 255) ):

        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
            

    def draw_text_defoult(self, text, size, x, y,color= (255, 255, 255) ):

        font = pygame.font.Font(self.font_named,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
    
    def draw_image(self, path, x, y ):
        bg = pygame.transform.scale(pygame.image.load(path), (100, 100))
        self.display.blit(bg, (x, y)) #location 

        # img = pygame.image.load(path)                
        # img_center = x, y
        # self.display.blit(img, img.get_rect(center=img_center))
         
# pygame.event.get() -> this basically goes through a list of everything the player can do on the computer 