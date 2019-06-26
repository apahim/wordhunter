"""
Matrix utilities and operations
"""

import random


def generate(dimension):
    """
    Generates a matrix of dimension x dimension elements. Each
    element is a random character from the alphabet, in lower case.

    :param dimension: the matrix dimension size
    :return:
    """
    return [[random.choice('abcdefghijklmnopqrstuvwxyz')
             for _ in range(dimension)]
            for _ in range(dimension)]
