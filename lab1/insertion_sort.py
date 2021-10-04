"""
Module to perform Insertion Sort
"""

import time


def insertion_sort(array: list) -> list:
    """
    Return sorted list, name of sorting method, number of comparisons
    and execution time using Insertion Sort method
    """
    name = "Insertion sort"
    comparisons = 0
    start = time.time_ns()
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            comparisons += 1
        array[j + 1] = key
        if j >= 0:
            comparisons += 1
    waiting = time.time_ns() - start

    return array, name, comparisons, waiting
