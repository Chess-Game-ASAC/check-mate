import os
class Piece:
    def init(self,name,color,image=None,image_rect=None): 
        self.name=name
        self.color=color
        self.image=image
        self.set_image()
        self.image_rect=image_rect

    def setimage(self):
        self.image = os.path.join(
            f'images/imgs-80px/{self.color}{self.name}.png')

class Pawn(Piece):
       def init(self, color):
        super().init('pawn', color)


class Knight(Piece):

    def init(self, color):
        super().init('knight', color)

class Bishop(Piece):

    def init(self, color):
        super().init('bishop', color)

class Rook(Piece):

    def init(self, color):
        super().init('rook', color)

class Queen(Piece):

    def init(self, color):
        super().init('queen', color)

class King(Piece):

    def init(self, color):

        super().init('king', color)