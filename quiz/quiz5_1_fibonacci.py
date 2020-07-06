"""
피보나치
"""


def fibonacci(n, memo=None):
    if memo is None:
        memo = {}

    if n <= 2:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


print(fibonacci(10))
