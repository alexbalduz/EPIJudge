from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    stack = []
    operators = {
        ']': '[',
        '}': '{',
        ')': '('
    }

    for item in s:
        if item in operators.values():
            stack.append(item)
        if item in operators:
            if not stack or operators[item] != stack.pop():
                return False
    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
