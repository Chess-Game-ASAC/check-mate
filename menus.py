import pygame

pygame.init()  # built in pygame functionality


WIDTH = 600
HEIGHT = 600
fps = 60  # frame rate 

timer = pygame.time.Clock()  # set up the timer in the beginning , actualy going to control how fast the game moves
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Check Mate')
main_menu = False
font = pygame.font.Font('freesansbold.ttf', 24) # font type & font size
bg = pygame.transform.scale(pygame.image.load('logo-checkmate.PNG'), (50, 50))
ball = pygame.transform.scale(pygame.image.load('logo-checkmate.PNG'), (50, 50))
menu_command = 0



class Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))

    def draw(self):
        pygame.draw.rect(screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark gray', [self.pos[0], self.pos[1], 260, 40], 5, 5)
        text2 = font.render(self.text, True, 'black')
        screen.blit(text2, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

def draw_menu(): 
    command = -1
    pygame.draw.rect(screen, 'beige', [100, 100, 300, 300]) 
    screen.blit(bg, (200, 50))
    # pygame.draw.rect(screen, 'green', [100, 100, 300, 300], 5)
    pygame.draw.rect(screen, 'white', [120, 120, 260, 40], 0, 5)
    # pygame.draw.rect(screen, 'light gray', [230, 450, 260, 40], 0, 5)
    pygame.draw.rect(screen, 'gray', [120, 120, 260, 40], 5, 5)
    txt = font.render('Menus Tutorial!', True, 'black')
    screen.blit(txt, (135, 127))
    # menu exit button
    menu = Button('Exit Menu', (120, 350))
    menu.draw()
    button1 = Button('Start Game', (120, 180))
    button1.draw()
    button2 = Button('Button 2', (120, 240))
    button2.draw()
    button3 = Button('Button 3', (120, 300))
    button3.draw()
    if menu.check_clicked():
        command = 0
    if button1.check_clicked():
        command = 1
    if button2.check_clicked():
        command = 2
    if button3.check_clicked():
        command = 3
    return command


def draw_game(): 
    menu_btn = Button('Main Menu', (230, 450))
    menu_btn.draw()
    menu = menu_btn.check_clicked()
    screen.blit(ball, (175, 175))
    return 


run = True
while run:
    screen.fill('beige')
    timer.tick(fps)

    # if main_menu var. we made is true then we will make the function draw_menu() run
    if main_menu:  
        menu_command = draw_menu()
        if menu_command != -1:
            main_menu = False

    else:
        main_menu = draw_menu()
        if menu_command > 0:
            text = font.render(f'Button {menu_command} pressed!', True, 'black')
            screen.blit(text, (150, 100))

    for event in pygame.event.get():
        if event.type ==pygame.MOUSEBUTTONDOWN:
            col,row=event.pos
            print (col, row)
            if row  >=180 and row <=220 and col >=120 and col<=380:
                enter_game= True
         
        if event.type == pygame.QUIT:
            run = False
        

    pygame.display.flip()  # come down outside of that event loop
pygame.quit()  # then even outside say quit 
               # which means the run variable has now been set equal to false 
               # so we exit this while loob and then quit out of the app 