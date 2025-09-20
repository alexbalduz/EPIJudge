from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    further_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= further_reach_so_far and further_reach_so_far < last_index:
        further_reach_so_far = max(further_reach_so_far, A[i] + i)
        i += 1
    return further_reach_so_far >= last_index



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
