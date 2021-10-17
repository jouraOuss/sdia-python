from sdia_python.lab2.utils import get_random_number_generator
import numpy as np
from scipy.special import gamma 

class BallWindow:
    def __init__(self, center, radius):
        """ create a new ball window
        Args : 
            center : type(float array) : coordinates of the center of the ball window.
            radius : type(float) : radius of the ball window 
        """
        self.center = center
        self.radius = radius

    def dimension(self):
        """Returns the dimension of the ball window 
        Args :
            center : type(float array)  : coordinates of the center of the ball window.
        Returns :
            dimension : type(int) : The length of the center of the ball window.
        """
        return len(self.center)

    def distance_to_center(self, point):
        """ Returns the distance between the center of the ball window and a point of interest
        Args: 
            point : type(float array) : coordinates of the point test.
        Returns : 
            distance_to_center : type(float) : the distance between the center and the given point of interest.
        """
        if len(point) != len(self.center) :
            raise ValueError("the size of the point is different from the len of the ball")
        else : 
            return np.linalg.norm(point-self.center)
    def __contains__(self, point):
        """ Returns True if a point of interest is inside the ball window.
        Args : 
            point : type(float array) : coordinates of the point test.
        Returns : 
            True if the point of interest is inside the ball window
        """
        if len(point) != len(self.center) :
            raise ValueError("the size of the point is different from the len of the ball")
        else : 
            if self.distance_to_center(point) < self.radius : 
                return True
            return False

    def surface(self):
        """ Returns the value of the surface of the ball window
        Args  : 
            radius : type(float) : the radius of the ball window.
            center : type(float array) : coordinates of the center of the ball window.
        Returns :
            surface type(float) : The surface of the ball window.
        """
        n = len(self.center)
        R = self.radius
        return 2 * (3.14) ** (n / 2) * R ** (n - 1) / gamma(n / 2)

    class UnitBallWindow(BallWindow):
        def __init__(self, center):

            super().__init__(center, 1)