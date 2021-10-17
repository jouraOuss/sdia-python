import numpy as np
import pytest

from sdia_python.lab2.box_window import BoxWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()

@pytest.mark.parametrize(
    "point, expected",[
        (np.array([0, 0]), True),
        (np.array([2.5, 2.5]), True),
        (np.array([-1, 5]), False), 
        (np.array([10, 3]), False),
     ],
)
def test_indicator_function(point, expected):
    box = BoxWindow([[0, 5], [0, 5]])
    is_in = box.indicator_function(point)
    assert is_in == expected


# ================================
# ==== WRITE YOUR TESTS BELOW ====
# ================================
@pytest.mark.parametrize(
    "bounds, expected", [
        (np.array([[2., 4.], [1., 3.]]), 4.0),
        (np.array([[1., 5.], [0., 2.], [10., 20.]]), 80.0),
        ],
)
def test_box_volume(bounds, expected):
    assert BoxWindow(bounds).volume() == expected

@pytest.mark.parametrize(
    "bounds, expected", [
        
        (np.array([[0.1, 4], [1, 3.5]]), 2),
        (np.array([[0, 5], [-0.33, 2.155], [-12, 15]]), 3,),
        ],
)
def test_box_dimension(bounds, expected):
    assert BoxWindow(bounds).dimension() == expected

    
@pytest.mark.parametrize(
    "box, expected",
    [
        (np.array([[1, 2], [0, 2]]), np.array([1.5, 1.])),
        (np.array([[0, -4], [4, 5], [1, 3]]), np.array([-2. ,  4.5,  2. ])),
        (np.array([[1, 2], [0, 2], [-4, 4], [1, 2]]), np.array([1.5, 1. , 0. , 1.5])),
    ],
)
def test_center(box, expected):
    assert (BoxWindow(box).center() == expected).all()

