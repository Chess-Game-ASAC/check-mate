class Move :
    """
    this class to save the start and end move 
    """
    def __init__(self, start , end ):
        self.start= start  #{row:,col:}
        self.end=end       #{row:,col:}

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

   