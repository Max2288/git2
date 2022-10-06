"""This file contains all functions that help us in the future."""
import numpy as np


def opredelitel_first_order(mat_first_order: list):
    """Count first order determinant.

    Args:
        mat_first_order (list): matrix where we count it.

    Returns:
        elem (int): first order determinant.
    """
    try:
        elem = int(mat_first_order[0][0])
    except Exception:
        return 'Код написан для матриц, состоящих из цифр'
    else:
        return elem


def opredelitel_second_order(mat_second_order: list):
    """Count second order determinant.

    Args:
        mat_second_order (list): matrix where we count it.

    Returns:
        elem (int): second order determinant.
    """
    try:
        our_sum = 0
        for elem in mat_second_order:
            our_sum += sum(elem)
    except Exception:
        return 'Код написан для матриц, состоящих из цифр'
    else:
        return mat_second_order[0][0] * mat_second_order[1][1] - \
            mat_second_order[0][1] * mat_second_order[1][0]


def opredelitel_third_order(mat_third_order: list):
    """Count third order determinant.

    Args:
        mat_third_order (list): matrix where we count it.

    Returns:
        elem (int): third order determinant.
    """
    try:
        our_sum = 0
        for elem in mat_third_order:
            our_sum += sum(elem)
    except Exception:
        return 'Код написан для матриц, состоящих из цифр'
    else:
        third_order = 0

        strikethrough_line = 0

        for strikethrough in range(3):

            mat_new = mat_third_order.copy()

            mat_new.pop(strikethrough_line)

            for num, _ in enumerate(mat_new):

                mat_new[num] = mat_new[num][:strikethrough] + mat_new[num][strikethrough + 1:]

            third_order += (-1)**(strikethrough_line + strikethrough + 2) * \
                mat_third_order[strikethrough_line][strikethrough] * opredelitel_second_order(mat_new)

        return third_order


def fib(number: int):
    """Count any fibonacci number.

    Args:
        number (int): place of number of fibonacci

    Returns:
        result_matrix (int): number of fibonacci
    """
    if number < 2 and number > -2:
        return number
    negative = False
    if number < 0:
        negative = True
        number = abs(number)

    single_matrix = np.matrix([[0, 1], [1, 1]], dtype=object)
    new_matrix = pow(single_matrix, number - 1)
    result_matrix = new_matrix * np.matrix([[0], [1]])
    if negative and (abs(number) + 1) % 2 != 0:
        return int(-result_matrix[1])
    else:
        return int(result_matrix[1])
