from typing import List

from test_framework import generic_test
import math


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n = len(partial_assignment)

    if any(
        has_duplicate([partial_assignment[i][j] for j in range(n)])
        or has_duplicate([partial_assignment[j][i] for j in range(n)])
        for i in range(n)
    ):
        return False

    region_size = int(math.sqrt(len(partial_assignment)))
    return all(not has_duplicate([
        partial_assignment[a][b]
        for a in range(region_size * i, region_size * (i + 1))
        for b in range(region_size * j, region_size * (j+1))
    ]) for i in range(region_size) for j in range(region_size))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
