import pytest
from sorted_array import (
    my_sort,
    bubble_sort,
    insertion_sort,
    selection_sort,
    SortedArray,
    binary_search,
)


# --------------------------
# ТЕСТЫ сортировок
# --------------------------

@pytest.mark.parametrize("sort_func", [my_sort, bubble_sort, insertion_sort, selection_sort])
@pytest.mark.parametrize("arr, expected", [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([3, 1, 2], [1, 2, 3]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([10, -1, 7, 3], [-1, 3, 7, 10]),
    ([2, 2, 2], [2, 2, 2]),
    ([17, 5, 4, 9, 3, 2, 1, 12], [1, 2, 3, 4, 5, 9 ,12 ,17]),
    ([1, 2, -100, 3, -100, 4, 5], [-100, -100, 1, 2, 3, 4, 5]),
])
def test_sorting_algorithms(sort_func, arr, expected):
    """Проверяем корректность всех сортировок"""
    assert sort_func(arr) == expected


# --------------------------
# ТЕСТЫ SortedArray (insert, delete, get, has)
# --------------------------

def test_sorted_array_insert_and_repr():
    arr = SortedArray([3, 1, 2])
    assert arr.data == [1, 2, 3]

    arr.insert(4)
    assert arr.data == [1, 2, 3, 4]

    arr.insert(0)
    assert arr.data == [0, 1, 2, 3, 4]

    arr.insert(2)
    assert arr.data == [0, 1, 2, 2, 3, 4]

    assert "SortedArray" in repr(arr)


def test_sorted_array_delete():
    arr = SortedArray([1, 2, 3, 4])
    arr.delete(3)
    assert arr.data == [1, 2, 4]

    arr.delete(99)  # удаление несуществующего
    assert arr.data == [1, 2, 4]


def test_sorted_array_get():
    arr = SortedArray([10, 5, 7])
    assert arr.get(0) == 5
    assert arr.get(1) == 7
    assert arr.get(2) == 10


def test_sorted_array_has():
    arr = SortedArray([1, 3, 5, 7])
    assert arr.has(3) is True
    assert arr.has(4) is False
    arr.insert(4)
    assert arr.has(4) is True


# --------------------------
# ТЕСТЫ binary_search
# --------------------------

def test_binary_search_found():
    arr = SortedArray([1, 3, 5, 7, 9])
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 5) == 2
    assert binary_search(arr, 9) == 4


def test_binary_search_not_found():
    arr = SortedArray([1, 3, 5, 7, 9])
    assert binary_search(arr, -1) == -1
    assert binary_search(arr, 2) == -1
    assert binary_search(arr, 10) == -1


def test_binary_search_empty_array():
    arr = SortedArray([])
    assert binary_search(arr, 1) == -1
