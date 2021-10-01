"""
Module to test the efficiency of different sorting algorithms
"""


def insertion_sort(array: list) -> list:
    """
    Return sorted list using Insertion Sort method
    """
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return array


def selection_sort(array: list) -> list:
    """
    Return sorted list using Selection Sort method
    """
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

    return array


def shell_sort(array: list) -> list:
    """
    Return sorted list using Shell Sort method
    """
    gap = len(array) // 2
    while gap > 0:
        i = 0
        j = gap

        while j < len(array):

            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

            i += 1
            j += 1
            k = i
            while k - gap > -1:

                if array[k - gap] > array[k]:
                    array[k-gap], array[k] = array[k], array[k-gap]
                k -= 1
        gap //= 2

    return array


def merge_sort(array: list) -> list:
    """
    Return sorted list using Shell Sort method
    """
    if len(array) > 1:

        mid = len(array)//2

        L = array[:mid]
        R = array[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    return array


if __name__ == "__main__":
    array = [1, 5, -10, 4, 76, 34, 100, 4, 7, 2, 15]
    print(insertion_sort(array))
    print(selection_sort(array))
    print(shell_sort(array))
    print(merge_sort(array))
