# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
    matrix = []
    for xi in x:
        basis = []
        for j in range(degree + 1):
            basis.append(np.polynomial.polynomial.Polynomial.basis(j)(xi))
        matrix.append(basis)
    return np.array(matrix)
