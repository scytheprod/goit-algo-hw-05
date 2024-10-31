from functools import cache


def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 0:
            return 1
        elif n in (1,2):
            return 1
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci

fib = caching_fibonacci()
print(fib(10))





