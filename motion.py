import pygame

class Motion :
    """
    this class for move the pieces have:
    3 attribute : col_y,row_x,piece,M_row,M_col
    4 method    :update_screen(),update(),save_piece(),delete_piece():
    """
    def __init__(self):
        self.col_y=None #Save the column for the piece you clicked on
        self.row_x=None  #Save the row for the piece you clicked on
        self.piece=None  #Save the piece you clicked on
        self.M_row=None  #Save the row you motion on it
        self.M_col=None  #Save the column you motion on it
        self.moving= False
 
    # MOUSEMOTION event
    def MouseMotion(self,col,row):
        self.M_row=row
        self.M_col=col
    def update_screen(self,surface):
        """
        this method used in MOUSE MOTION event to display the piece when you motion the mouse and before MOUSE BUTTON UP
        take 3 arguments :
        row =event.pos[1]
        col=event.pos[0]
        surface : screen to display the board and pieces
        """
        path=self.piece.image  # find the path for the move piece
        img=pygame.image.load(path) # show the pices as image
        img_center = self.M_col, self.M_row  #  make the center of piece's image equal the mouse position
        
        self.piece.image_rect = img.get_rect(center=img_center)  # use to show the piece
        surface.blit(img, self.piece.image_rect)  # function in pygame library  to display the pieces on the board


    # MOUSE BUTTON DOWN event
    def update(self,row,col):
        """
        save the coordinates for the click mouse 
        row=event.pos[1]//75
        col=event.pos[0]//75
        """
        self.col_y=col
        self.row_x=row

    def save_piece(self,piece):
        """
        save the piece that you clicked on it 
        """
        self.piece=piece
        self.moving= True
    # MOUSE BUTTON UP event
    def delete_piece(self):
        """
        to delete the piece ,M_row,M_col after MOUSE BUTTON UP
        """
        self.piece=None
        self.M_row=None
        self.M_col=None
        self.moving= False


