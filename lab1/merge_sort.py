"""
Module to perform Merge Sort
"""

import time


def merge_sort(array: list) -> tuple:
    """
    Return sorted list, name of sorting method, number of comparisons
    and execution time using Merge Sort method
    """
    name = "Merge sort"
    comparisons = 0
    start = time.time_ns()

    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        comparisons += merge_sort(left)[2]
        comparisons += merge_sort(right)[2]

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            comparisons += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    waiting = time.time_ns() - start
    return array, name, comparisons, waiting
