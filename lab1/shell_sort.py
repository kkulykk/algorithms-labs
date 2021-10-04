"""
Module to perform Shell Sort
"""

import time


def shell_sort(array: list) -> tuple:
    """
    Return sorted list, name of sorting method, number of comparisons
    and execution time using Shell Sort method
    """
    name = "Shell sort"
    comparisons = 0
    array_length = len(array)
    start = time.time_ns()
    h = array_length // 2
    while h > 0:
        for i in range(h, array_length):
            element = array[i]
            k = i
            while k >= h and array[k - h] > element:
                comparisons += 1
                array[k] = array[k - h]
                k -= h
            array[k] = element
            if k >= h:
                comparisons += 1
        h = h // 2
    waiting = time.time_ns() - start

    return array, name, comparisons, waiting
