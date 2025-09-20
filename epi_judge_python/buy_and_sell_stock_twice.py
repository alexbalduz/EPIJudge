from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    # Forward pass: best profit until each day
    min_price_so_far, max_profit = float('inf'), 0.0
    max_profit_until = [0.0] * len(prices)
    for i in range(len(prices)):
        max_profit = max(max_profit, prices[i] - min_price_so_far)
        max_profit_until[i] = max_profit
        min_price_so_far = min(min_price_so_far, prices[i])

    # Backward pass: best profit from each day
    max_price_so_far = float('-inf')
    for i in reversed(range(len(prices))):
        max_profit = max(max_profit, max_price_so_far - prices[i] + max_profit_until[i])
        max_price_so_far = max(max_price_so_far, prices[i])

    return max_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
