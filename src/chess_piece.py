import os
class Piece:
    """
    This class to create the chess pieces have :
    4 attribute : name,color,image,imag_rect
    1 method    
    """
    def __init__(self,name,color,image=None,image_rect=None): 
        self.name=name   #the name of piece
        self.color=color #the color of piece
        self.image=image #the path of pecies image 
        self.set_image()
        self.image_rect=image_rect

    def set_image(self):
        """
        this methode to creat the path of the pecie image 
        """
        self.image = os.path.join(
            f'images/imgs-80px/{self.color}_{self.name}.png')

class King(Piece):
    """
    this class Inherit from Piece class and creat the path to king Piece
    """
    def __init__(self, color):
        super().__init__('king', color)

class Queen(Piece):
    """
    this class Inherit from Piece class and creat the path to queen Piece
    """

    def __init__(self, color):
        super().__init__('queen', color)


class Knight(Piece):
    """
    this class Inherit from Piece class and creat the path to knight Piece
    """

    def __init__(self, color):
        super().__init__('knight', color)

class Bishop(Piece):
    """
    this class Inherit from Piece class and creat the path to bishop Piece
    """

    def __init__(self, color):
        super().__init__('bishop', color)

class Rook(Piece):
    """
    this class Inherit from Piece class and creat the path to rook Piece
    """

    def __init__(self, color):
        super().__init__('rook', color)

class Pawn(Piece):
    """
    this class Inherit from Piece class and creat the path to Pawn Piece
    """
    def __init__(self, color):
        super().__init__('pawn', color)

