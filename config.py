import os
# import pygame
from sound import Sound



from settings import *


class Config:

    def __init__(self):
        self.themes = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.move_sound = Sound(
            os.path.join('sounds\move.wav'))
        self.capture_sound = Sound(
            os.path.join('sounds\capture.wav'))

    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    def _add_themes(self):
        green = Theme((251, 250, 205), (230, 186, 149), '#AABBCC', '#89AACB', '#FF8DD1', '#FFADBC')
        brown = Theme('#FCE0D1','#DC9A67', '#AABBCC', '#89AACB', '#FF8DC7', '#FFADBC')
        blue = Theme('#C3C6BE', '#727FA2', '#AABBCC', '#89AACB', '#FF8DC7', '#FFADBC')
        gray = Theme('#FFFFFF', '#58AC8A', '#AABBCC', '#89AACB', '#FF8DC7', '#FFADBC')
        self.themes = [green, blue,brown, gray]

        