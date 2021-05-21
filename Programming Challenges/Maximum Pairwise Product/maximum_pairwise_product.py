# python3
# import random


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    n = len(numbers)
    first_max_index = -1

    for index in range(n):
        if (first_max_index == -1) or (numbers[index] > numbers[first_max_index]):
            first_max_index = index

    second_max_index = -1
    for index in range(n):
        if index != first_max_index and (second_max_index == -1 or numbers[index] > numbers[second_max_index]):
            second_max_index = index

    return numbers[first_max_index] * numbers[second_max_index]


if __name__ == '__main__':
    # while True:
    #     _n = random.randint(2, 10)
    #     print(f'{_n}')
    #     a = []
    #     for i in range(0, _n):
    #         a.append(random.randint(10, 100000))
    #     for i in range(0, _n):
    #         print(f'{a[i]}  ', end='')
    #     print('\n')
    #     _res_a = max_pairwise_product_naive(a)
    #     _res_b = max_pairwise_product(a)
    #
    #     if _res_a != _res_b:
    #         print(f'Wrong Answer: {_res_a} {_res_b}')
    #         break
    #     else:
    #         print('OK\n')

    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
