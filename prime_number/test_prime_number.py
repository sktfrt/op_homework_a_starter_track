import time
import pytest
from prime_number import is_prime, is_prime_fast, find_largest_prime


# --------------------------
# ТЕСТЫ is_prime и is_prime_fast
# --------------------------

@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (9, False),
    (11, True),
    (25, False),
    (29, True),
    (1, False),
    (0, False),
    (653, True),
    (657, False),
    (9973, True),
    (9974, False),
    (-7, False),
])
def test_is_prime_basic(n, expected):
    assert is_prime(n) == expected


@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (9, False),
    (11, True),
    (25, False),
    (29, True),
    (1, False),
    (0, False),
    (653, True),
    (657, False),
    (9973, True),
    (9974, False),
    (-7, False),
])
def test_is_prime_fast_basic(n, expected):
    assert is_prime_fast(n) == expected


def test_is_prime_and_fast_are_equivalent():
    """Обе функции должны давать одинаковый результат на диапазоне чисел"""
    for n in range(0, 200):
        assert is_prime(n) == is_prime_fast(n)


# --------------------------
# ТЕСТЫ find_largest_prime
# --------------------------

@pytest.mark.parametrize("limit, expected", [
    (10, 7),   # простые числа: 2, 3, 5, 7
    (20, 19),
    (30, 29),
    (2, 2),
    (10_000, 9973),
    (50_050, 50_047),
    (1, -1),   # нет простых чисел
])
def test_find_largest_prime(limit, expected):
    assert find_largest_prime(limit, use_fast=False) == expected
    assert find_largest_prime(limit, use_fast=True) == expected


# --------------------------
# ТЕСТ на производительность
# --------------------------

def test_fast_method_is_faster():
    """
    Проверяем, что is_prime_fast реально быстрее на больших числах.
    Сравниваем время 10 запусков поиска наибольшего простого числа.
    """
    limit = 50_000_000
    runs = 10

    start = time.time()
    for _ in range(runs):
        find_largest_prime(limit, use_fast=False)
    naive_time = time.time() - start

    start = time.time()
    for _ in range(runs):
        find_largest_prime(limit, use_fast=True)
    fast_time = time.time() - start

    print(f"\nNaive: {naive_time:.4f} sec, Fast: {fast_time:.4f} sec")

    assert fast_time < naive_time
