from functions import opredelitel_first_order
from functions import opredelitel_second_order
from functions import opredelitel_third_order
from functions import fib
import pytest

test_for_opr_first = []
with open('testforopredelitel1.txt', 'r') as file_opr_first:
    new_lst = file_opr_first.readlines()
    for string in new_lst:
        list_of_str = []
        for elem in string.split(':'):
            list_of_str.append(elem)
        list_of_str[0] = list_of_str[0].replace(',', '').\
            replace('[', '').replace(']', '').split()
        list_of_str[0] = [int(new_elem) for new_elem in list_of_str[0]]
        string = ([[list_of_str[0][dig]]for dig in range(0, len(list_of_str[0]))],\
                int(list_of_str[1].replace('\n', '')))
        test_for_opr_first.append(string)


@pytest.mark.parametrize('test_inp, expect', test_for_opr_first)
def test_determinant_first(test_inp: list, expect: int):
    """Found determinant.

    Args:
        test_inp (list): test input for function.
        expect (int): test expecpection for function.
    """
    assert opredelitel_first_order(test_inp) == expect


test_for_opr_second = []
with open('testforopredelitel2.txt', 'r') as file_opr_second:
    new_lst = file_opr_second.readlines()
    for string in new_lst:
        list_of_str = []
        for elem in string.split(':'):
            list_of_str.append(elem)
        list_of_str[0] = list_of_str[0].replace(',', '').replace('[', '').replace(']', '').split()
        list_of_str[0] = [int(new_elem) for new_elem in list_of_str[0]]
        string = ([[list_of_str[0][dig], list_of_str[0][dig + 1]]\
                 for dig in range(0, len(list_of_str[0]), 2)],\
                int(list_of_str[1].replace('\n', '')))
        test_for_opr_second.append(string)


@pytest.mark.parametrize('test_inp, expect', test_for_opr_second)
def test_determinant_second(test_inp: list, expect: int):
    """Found determinant.

    Args:
        test_inp (list): test input for function.
        expect (int): test expecpection for function.
    """
    assert opredelitel_second_order(test_inp) == expect


test_for_opr_third = []
with open('testforopredelitel3.txt', 'r') as file_opr_third:
    new_lst = file_opr_third.readlines()
    for string in new_lst:
        list_of_str = []
        for element in string.split(':'):
            list_of_str.append(element)
        list_of_str[0] = list_of_str[0].replace(',', '').replace('[', '').replace(']', '').split()
        list_of_str[0] = [int(new_elem) for new_elem in list_of_str[0]]
        string = ([[list_of_str[0][dig], list_of_str[0][dig + 1], list_of_str[0][dig + 2]]\
                 for dig in range(0, len(list_of_str[0]), 3)],\
                int(list_of_str[1].replace('\n', '')))
        test_for_opr_third.append(string)


@pytest.mark.parametrize('test_inp, expect', test_for_opr_third)
def test_determinant_third(test_inp: list, expect: int):
    """Found determinant.

    Args:
        test_inp (list): test input for function.
        expect (int): test expecpection for function.
    """
    assert opredelitel_third_order(test_inp) == expect


test_for_fib = []
with open('testfib.txt', 'r') as file_fib:
    test_for_fib = file_fib.readlines()
    for index, _ in enumerate(test_for_fib):
        test_for_fib[index] = test_for_fib[index].replace('\n', '')
        list_of_str = [int(new_elem) for new_elem in test_for_fib[index].split(':')]
        test_for_fib[index] = (list_of_str[0], list_of_str[1])


@pytest.mark.parametrize('test_inp, expect', test_for_fib)
def test_fib(test_inp: int, expect: int):
    """Test for fibonacci numbers.

    Args:
        test_inp (int): test input for function.
        expect (int): test expecpection for function.
    """
    assert fib(test_inp) == expect
