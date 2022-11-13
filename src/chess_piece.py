import os
class Piece:
    def __init__(self,name,color,image=None,image_rect=None): 
        self.name=name
        self.color=color
        self.image=image
        self.set_image()
        self.image_rect=image_rect

    def set_image(self):
        self.image = os.path.join(
            f'images/imgs-80px/{self.color}_{self.name}.png')

class Pawn(Piece):
       def __init__(self, color):
        super().__init__('pawn', color)


class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color)

class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color)

class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color)

class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color)

class King(Piece):

    def __init__(self, color):

        super().__init__('king', color)