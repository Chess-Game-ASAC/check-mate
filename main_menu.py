from game_menu import *
    
g = GameW()

while g.running:
    # g.curr_menu.display_menu()
    # g.playing = True

    g.curr_menu.display_menu()
    g.game_loop()
