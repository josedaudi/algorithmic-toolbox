# python3


def fibonacci_number_naive(n):
    print("Compute F sub", n)
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    if n <= 1:
        return n

    a, b, c = 0, 1, 0
    for _ in range(n - 1):
        c = a + b
        b, a = c, b
    return c


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
