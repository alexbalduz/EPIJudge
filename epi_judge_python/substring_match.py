from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    n, m = len(t), len(s)

    if m > n:
        return -1

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if t[i + j] != s[j]:
                match = False
                break

        if match:
            return i

    return -1

    # Other solution O(n^2)
    # for i in range(len(t)):
    #     for j in range(len(s)):
    #         if t[i] == s[j]:
    #             return i


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
