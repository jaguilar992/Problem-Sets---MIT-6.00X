from ps7 import *
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
        pos=self.getRobotPosition()
        self.room.cleanTileAtPosition(pos)
        new_pos=pos.getNewPosition(self.angle, self.speed)
        x,y=new_pos.getX(),new_pos.getY()
        while xlabel:
            pass
