import ps7
import math
import random

import ps7_visualize
import pylab
from ps7_verify_movement27 import testRobotMovement

class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        new_pos=self.position.getNewPosition(self.direction,self.speed)
        if self.room.isPositionInRoom(new_pos):
            self.room.cleanTileAtPosition(new_pos)
            self.position=new_pos
        else:
            self.direction=360*random.random()

#Uncomment this line to see your implementation of StandardRobot in action!
testRobotMovement(StandardRobot, RectangularRoom)
