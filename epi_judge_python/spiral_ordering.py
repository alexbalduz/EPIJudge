from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    result = []
    n = len(square_matrix)
    left, right = 0, n - 1
    top, bottom = 0, n - 1

    while top <= bottom and left <= right:
        # Left to right
        for col in range(left, right + 1):
            result.append(square_matrix[top][col])
        # Top to bottom
        for row in range(top + 1, bottom + 1):
            result.append(square_matrix[row][right])
        # Right to left
        for col in range(right - 1, left - 1, -1):
            result.append(square_matrix[bottom][col])
        # Bottom to top
        for row in range(bottom -1, top, -1):
            result.append(square_matrix[row][left])

        left += 1
        right -= 1
        top += 1
        bottom -= 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))