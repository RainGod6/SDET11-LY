import pytest
from test_pytest.div import div


@pytest.mark.parametrize("num1,num2,except_result", {(10, 2, 5),
                                                     (1, 1, 1),
                                                     (1000000000000, 10, 100000000000),
                                                     (0, 10, 0),
                                                     (-9, 3, -3),
                                                     (-1, 1, -1),
                                                     (-500, -50, 10)
                                                     })
def test_div_int(num1, num2, except_result):
    assert div(num1, num2) == except_result


@pytest.mark.parametrize("num1,num2,except_result", {(10, 2.0, 5.0),
                                                     (9.9, 3, 3.3),
                                                     (1, 1.0, 1.0),
                                                     (20.8, 4.2, 5.4),
                                                     (1000000.00, 100, 10000.0),
                                                     (-1.0, 1, -1.0),
                                                     (-100, 10, -10),
                                                     (-5, -2, 2.5)
                                                     })
def test_div_float(num1, num2, except_result):
    assert div(num1, num2) == except_result


@pytest.mark.parametrize("num1,num2,except_result", {('abc', 1, None),
                                                     (888, 'a', None),
                                                     ('b', 'b', None),
                                                     (True, False, None)
                                                     })
def test_div_exception(num1, num2, except_result):
    assert div(num1, num2) == except_result


@pytest.mark.parametrize("num1,num2,except_result", {(1, 0, ZeroDivisionError),
                                                     (9.0, 0, ZeroDivisionError),
                                                     (100, 0.0, ZeroDivisionError)
                                                     })
def test_div_zero(num1, num2, except_result):
    with pytest.raises(except_result):
        div(num1, num2)
