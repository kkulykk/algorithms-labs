"""
Module to perform Selection Sort
"""

import time


def selection_sort(array: list) -> tuple:
    """
    Return sorted list, name of sorting method, number of comparisons
    and execution time using Selection Sort method
    """
    name = "Selection sort"
    comparisons = 0
    start = time.time_ns()
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            comparisons += 1
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    waiting = time.time_ns() - start

    return array, name, comparisons, waiting
