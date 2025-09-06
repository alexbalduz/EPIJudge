from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    def add(a, b):
        return a if b == 0 else add(a ^ b, (a & b) << 1)
    sum = 0
    while x:
        if x & 1:
            sum = add(sum, y)
        x, y = x >> 1, y << 1
    return sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
