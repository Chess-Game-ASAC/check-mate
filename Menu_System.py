import pygame
import os
from game_menu import *



class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x-50, self.cursor_rect.y+120) #X 

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h -30
        self.rulesx, self.rulesy = self.mid_w, self.mid_h +10
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 50
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True

        while self.run_display:

            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            # self.game.draw_text('Check Mate Game', 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 -300,"orange")
            # self.game.draw_text("Start Game", 20, self.startx, self.starty)
            # self.game.draw_text("Rules", 20, self.rulesx, self.rulesy)
            # self.game.draw_text("Game developer", 20, self.creditsx, self.creditsy)
            # # self.game.draw_image( os.path.join("team_photo/chess_game.png"), self.game.DISPLAY_W / 2+120, self.game.DISPLAY_H / 2 + 100,200,200 )
            # # self.game.draw_image( os.path.join("team_photo/chess_game2.png"), self.game.DISPLAY_W / 2-105, self.game.DISPLAY_H / 2 + 100,200,200 )
            # # self.game.draw_image( os.path.join("team_photo/chess_game3.png"), self.game.DISPLAY_W / 2-330, self.game.DISPLAY_H / 2 + 100,200,200 )
            # self.game.draw_image( os.path.join("team_photo/image.jpeg"), self.game.DISPLAY_W / 2-100, self.game.DISPLAY_H / 2 - 270,200,200 )
            ####################################################3
            self.game.draw_text('Check Mate Game', 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 -250,"orange")
            self.game.draw_text("Start Game", 20, self.startx , self.starty+120)
            self.game.draw_text("Rules", 20, self.rulesx, self.rulesy+120)
            self.game.draw_text("Game developer", 20, self.creditsx, self.creditsy+120)
            self.game.draw_image( os.path.join("team_photo/image.jpeg"), self.game.DISPLAY_W / 2-120, self.game.DISPLAY_H / 2 - 200,250,250 )
            
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        """
        this methode to Move between the rules to select the appropriate option using the keyboard:
        DOWN_KEY
        UP_KEY
        """
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.rulesx + self.offset, self.rulesy)
                self.state = 'rules'
            elif self.state == 'rules':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'rules':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.rulesx + self.offset, self.rulesy)
                self.state = 'rules'

    def check_input(self):
        """
        select the appropriate option by using START_KEY * Enter*
        """
        self.move_cursor()

        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True

            elif self.state == 'rules':
                self.game.curr_menu = self.game.rules

            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits

            self.run_display = False

class rulesMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w-123, self.mid_h - 100
        self.controlsx, self.controlsy = self.mid_w-7, self.mid_h -150
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('rules', 20, self.game.DISPLAY_W / 2-150, self.game.DISPLAY_H / 2 - 200,"orange")
            self.game.draw_text(" * reset the game Press       r ", 13, self.volx, self.voly)
            self.game.draw_text(" * use the mouse to move the pieces in chess board", 13, self.controlsx, self.controlsy)
            self.game.draw_text(" * back to main  press        back key", 13,  self.volx+30, self.voly+50)
            self.game.draw_text(" * changing themes  press        a", 13,  self.volx+10, self.voly+100)

            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
            

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            # self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Game developer', 20, self.game.DISPLAY_W / 2-150, self.game.DISPLAY_H / 2 - 300,"orange")
            self.game.draw_text_defoult('Walaa Atiyh', 20,self.game.DISPLAY_W / 2-150, self.game.DISPLAY_H / 2 - 200)
            self.game.draw_text_defoult("Noor Alkhateeb ", 20, self.game.DISPLAY_W / 2-150, self.game.DISPLAY_H / 2 - 80)
            self.game.draw_text_defoult("Abdalla Mosa ", 20, self.game.DISPLAY_W / 2-150, self.game.DISPLAY_H / 2+40 )
            self.game.draw_text_defoult("Dina ALshboul ", 20, self.game.DISPLAY_W / 2-150, self.game.DISPLAY_H / 2 +160)
            self.game.draw_text_defoult("Mohannad Jaser ", 20, self.game.DISPLAY_W / 2-150, self.game.DISPLAY_H / 2 + 280)
            self.game.draw_image( os.path.join("team_photo/walaa.jpg"), self.game.DISPLAY_W / 2+100, self.game.DISPLAY_H / 2 - 250 )
            self.game.draw_image( os.path.join("team_photo/noor.png"), self.game.DISPLAY_W / 2+100, self.game.DISPLAY_H / 2 - 130 )
            self.game.draw_image( os.path.join("team_photo/abdallh.png"), self.game.DISPLAY_W / 2+100, self.game.DISPLAY_H / 2 - 10 )
            self.game.draw_image( os.path.join("team_photo/dina.png"), self.game.DISPLAY_W / 2+100, self.game.DISPLAY_H / 2 +110 )
            self.game.draw_image( os.path.join("team_photo/mohannad.png"), self.game.DISPLAY_W / 2+100, self.game.DISPLAY_H / 2 +230 )
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        
    