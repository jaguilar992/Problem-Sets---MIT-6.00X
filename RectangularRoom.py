class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width=width
        self.height=height
        self.tiles_Map={}

        for i in range(self.width):
            for j in range(self.height):
                pos=(i,j)
                self.tiles_Map[pos]=False
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x_Tile=int(math.floor((pos.getX())))
        y_Tile=int(math.floor((pos.getY())))
        # if (x_Tile,y_Tile) in self.tiles_Map:
        self.tiles_Map[(x_Tile,y_Tile)]=True

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles_Map[(m,n)]

    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width*self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        count=0
        for i in self.tiles_Map.values():
            if i==True:
                count+=1
        return count


    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        rnd_x=self.width*random.random()
        rnd_y=self.height*random.random()
        return Position(rnd_x,rnd_y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        x=pos.getX()
        y=pos.getY()
        if x<self.width and x>=0:
            if y<self.height and y>=0:
                return True
            else:
                return False
        else:
            return False
