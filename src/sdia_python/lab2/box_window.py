from sdia_python.lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """Represents a box in any dimension by writing it as a product of segments."""

    def __init__(self, bounds):
        """Create a box window by initializing the bounds with as input parameters an np.array. The bounds must be given by np.array such that for each segment a <= b
        Args:
            bounds ([np.array]): An Array containing the bounds for each dimension
        """
        self.bounds = bounds

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`
        Returns:
            str : string representation of the box window
        """
        args = self.bounds
        ch = ""
        for i in range(0, len(args)):
            ch = ch + str(args[i])
            if i < len(args) - 1:
                ch += " x "

        return "BoxWindow : " + ch

    def __len__(self):
        """ Returns the number of points in the box.
        Args : type(int) : dimension of the box.
        """
        return 2 * len(self.bounds)

    def __contains__(self, sub_box):
        """ Return True if the box contains a given sub_box
        Args : sub_box : type(np.array) : The sub_box to be tested
        """
        Box_bounds = self.bounds
        sub_box_bounds = sub_box.bounds
        try:
            assert len(sub_box) == len(self)
        except:
            print("the size of the sub_box is different from that of the box")
        for i in range(0, len(point)):
            a = sub_box_bounds[i][0]
            b = sub_box_bounds[i][1]
            c = Box_bounds[i][0]
            d = Box_bounds[i][1]
            if a < c or d < b:
                return False
        return True

    def dimension(self):
        """Returns the dimension of our box
        Args : type(int) The dimension of the box
        """
        return len(self.bounds)

    def volume(self):
        """Computes the volume of our box, by mutliplying the difference between the arguments of every subsegment
        """

        return np.prod(np.diff(self.bounds, axis=1))

    def indicator_function(self, point):
        """Return True if a point is contained in the box

        Args:
            point (np.array): The point to be tested
        """
        Box_bounds = self.bounds
        n = len(Box_bounds)
        try:
            assert len(point) == len(self)
        except:
            print("the size of the point is different from the len of the box")
        for i in range(0, n):
            a = Box_bounds[i][1]
            b = Box_bounds[i][0]
            if point[i] < b or point[i] > a:
                return False
        return True

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.
        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        L = []
        for i in range(n):
            l = []
            for i in range(0, len(self.bounds)):
                a = (
                    self.bounds[j][1] - self.bounds[j][0]
                ) * rng.random() + self.bounds[j][0]
                l.append(a)
            L.append(l)
        return L

    def center(self):
        """Returns  a list containing the center of every segment of the box
        Returns:
            Center type(list): a list of numbers
        """
        return np.mean(self.bounds, axis=1)


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """Represents a box in any dimension. The lenght of every segment in the box is equal to 1, centered on `center`

        Args:
            dimension (int): the dimension of the box
            center (list): List containing the center of every segment in the box. Defaults to None.
        """
        L = []
        if center is None:
            center = np.zeros(dimension)
        else:
            for i in range(dimension):
                L.append([center[i] - 0.5, center[i] + 0.5])
        super().__init__(L)
