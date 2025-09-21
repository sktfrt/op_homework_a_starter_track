from typing import Optional
import random


def my_sort(arr: list[int]) -> list[int]:
    #nums = arr
    #sorted_nums = []
    
    while len(arr) != 0:
        min_num = arr.pop(arr.index(min(arr)))
        arr.append(min_num)
     
    return arr


def bubble_sort(arr: list[int]) -> list[int]:
    for i in range(0, len(arr)):
        swapped = False

        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break
    return arr


def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        val = arr[i]
        hole = i
        
        while hole > 0 and arr[hole - 1] > val:
            arr[hole] = arr[hole - 1]
            hole -= 1
        
        arr[hole] = val
    return arr


def selection_sort(arr: list[int]) -> list[int]:
    for i in range(0, len(arr)):
        current_min = arr[i]
        min_index = i

        for j in range(i, len(arr)):
            if arr[j] < current_min:
                current_min = arr[j]
                min_index = j
            
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def merge_sort(arr: list[int]) -> list[int]:
    pass


class SortedArray:
    data = []

    def __init__(self, data: Optional[list[int]] = []):
        self.data = selection_sort(data)
        

    def insert(self, value: int) -> None:
        self.data.append(value)
        self.data = selection_sort(self.data)
    

    def delete(self, value: int) -> None:
        try:
            self.data.remove(value)
        except:
            pass

    def get(self, index: int) -> int:
        return self.data[index]


    def has(self, value: int) -> bool:
        if binary_search(value) != -1:
            return True
        else: return False


def binary_search(sorted_arr: SortedArray, target: int) -> int:
    left = 0
    right = len(sorted_arr - 1)
    middle = (left + right) // 2

    while left < right:
        if sorted_arr[middle] == target:
            return middle
        elif sorted_arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
