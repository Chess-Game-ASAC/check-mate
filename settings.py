import pygame
class Color:

    def __init__(self, light, dark):
        self.light = light
        self.dark = dark


class Theme:

    def __init__(self, light_bg, dark_bg, 
                       light_trace, dark_trace,
                       light_moves, dark_moves):
        
        self.bg = Color(light_bg, dark_bg)
        self.trace = Color(light_trace, dark_trace)
        self.moves = Color(light_moves, dark_moves)



class Sound:

    def __init__(self, path):
        self.path = path
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        pygame.mixer.Sound.play(self.sound)