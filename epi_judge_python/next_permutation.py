from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    n = len(perm)

    i = n - 2
    while i >= 0 and perm[i] >= perm[i+1]:
        i -= 1

    if i == -1:
        return []

    j = n - 1
    while perm[i] >= perm[j]:
        j -= 1

    perm[i], perm[j] = perm[j], perm[i]

    perm[i+1:] = reversed(perm[i+1:])
    return perm

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
