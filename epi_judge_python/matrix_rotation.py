from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    for i in range(len(square_matrix)):
        for j in range(i + 1, len(square_matrix)):
            square_matrix[i][j], square_matrix[j][i] = square_matrix[j][i], square_matrix[i][j]

    for i in range(len(square_matrix)):
        square_matrix[i] = list(reversed(square_matrix[i]))


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
