from functions import opredelitel_1_poryadka
from functions import opredelitel_2_poryadka
from functions import opredelitel_3_poryadka
from functions import fib
import pytest

test_1 = [([[1]],1),([[5]],5),([[8]],8)]

@pytest.mark.parametrize('test_inp, expect',test_1)
def test_determinant_1(test_inp,expect):
    assert opredelitel_1_poryadka(test_inp) == expect

test_2 = [([[1, 3], [5, 4]], -11), ([[7, 10], [40, 5]], -365), ([[8, 1], [11, 6]], 37), ([[15, -7], [-11, 4]], -17)]

@pytest.mark.parametrize('test_inp, expect',test_2)
def test_determinant_2(test_inp,expect):
    assert opredelitel_2_poryadka(test_inp) == expect

test_3 = [([[15, -7,  5], [-1, 4,  4], [3, 6, 9]], -57), ([[13, -7,  -1], [-1, 7,  4], [3, 1, -9]], -870), ([[13, -7,  -10], [-1, 2,  4], [0, 1, -9]], -213)]

@pytest.mark.parametrize('test_inp, expect',test_3)
def test_determinant_3(test_inp,expect):
    assert opredelitel_3_poryadka(test_inp) == expect

test_for_fib = [(100,354224848179261915075),(5,5),(-7,13),(-8,-21)]

@pytest.mark.parametrize('test_inp, expect',test_for_fib)
def test_fib(test_inp, expect):
    assert fib(test_inp) == expect
