import numpy as np
from math import gamma


class BallWindow:
    """class BallWindow contains balls defined by centers and radius"""

    def __init__(self, center, radius):
        """initialization
        Args:
            center (array): the center
            R (float): radius of the ball
        """
        try:
            assert radius >= 0
        except:
            print("Enter a positive radius")

        try:
            # This will detect problems with center
            assert len(center) > 0
        except:
            print("Enter a valid center")
        self.center = np.array(center, dtype=np.float32)
        self.radius = radius

    def __str__(self):
        """ print the ball
        Returns:
            str: BallWindow: center=, radius=
        """

        float_formatter = "{:.2f}".format
        np.set_printoptions(formatter={"float_kind": float_formatter})
        return (
            "BallWindow: "
            + "center="
            + str(self.center)
            + ", radius="
            + str("%.2f" % round(self.radius, 2))
        )

    def indicator(self, point):
        """ Returns True if a point of interest is inside the ball window.
        Args :
            point : type(float array) : coordinates of the point test.
        Returns :
            True if the point of interest is inside the ball window
        """
        try:
            assert self.dimension() == len(point)
        except:
            print("dimension error")
        return np.sum((point - self.center) ** 2) <= self.radius ** 2

    def dimension(self):
        """ball dimensions
        Returns:
            int: dimension
        """
        return len(self.center)

    def volume(self):
        """ Returns the value of the volume of the ball window
        Args  :
            radius : type(float) : the radius of the ball window.
            center : type(float array) : coordinates of the center of the ball window.
        Returns :
            volume type(float) : The volume of the ball window.
        """
        return (
            (np.pi ** (self.dimension() / 2))
            * (self.radius ** self.dimension())
            / (gamma(self.dimension() / 2 + 1))
        )


class UnitBallWindow(BallWindow):
    """representing a ball of radius==1
    """

    def __init__(self, center):

        super().__init__(center, radius=1)
