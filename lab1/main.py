"""
Module to test the efficiency of different sorting algorithms
"""

import random
import matplotlib.pyplot as plt
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from shell_sort import shell_sort
from merge_sort import merge_sort


def generate_array(mode: str, size: int) -> list:
    """
    Return a list with given parameters
    """
    array = [i for i in range(size)]
    if mode == "random_array":
        return [random.randint(1, 10000) for _ in range(size)]
    elif mode == "sorted_array":
        return array
    elif mode == "reversed_array":
        return array[::-1]
    elif mode == "repeating_array":
        return [random.randint(1, 3) for _ in range(size)]


def test_case_1(algorithm) -> tuple:
    """
    Perform test No. 1 with random array
    """
    size = 2
    results = {}
    for i in range(9):
        average_time = 0
        average_comparisons = 0
        for _ in range(5):
            array = generate_array("random_array", size)
            execution_result = algorithm(array)
            average_time += execution_result[3]
            average_comparisons += execution_result[2]
        results[7 + i] = (
            int(average_comparisons / 5), average_time / 5)
        size *= 2
    return 'EXPERIMENT 1 (RANDOM ARRAY)', execution_result[1], results


def test_case_2(algorithm) -> tuple:
    """
    Perform test No. 2 with sorted array
    """
    size = 2
    results = {}
    for i in range(9):
        array = generate_array("sorted_array", size)
        execution_result = algorithm(array)
        results[7 + i] = (
            int(execution_result[2]), int(execution_result[3]))
        size *= 2
    return 'EXPERIMENT 2 (SORTED ARRAY)', execution_result[1], results


def test_case_3(algorithm) -> tuple:
    """
    Perform test No. 3 with reversed array
    """
    size = 2
    results = {}
    for i in range(9):
        array = generate_array("reversed_array", size)
        execution_result = algorithm(array)
        results[7 + i] = (
            int(execution_result[2]), int(execution_result[3]))
        size *= 2
    return 'EXPERIMENT 3 (REVERSED ARRAY)', execution_result[1], results


def test_case_4(algorithm) -> tuple:
    """
    Perform test No. 4 with repeating array
    """
    size = 2
    results = {}
    for i in range(9):
        average_time = 0
        average_comparisons = 0
        for _ in range(3):
            array = generate_array("repeating_array", size)
            execution_result = algorithm(array)
            average_time += execution_result[3]
            average_comparisons += execution_result[2]
        results[7 + i] = (
            int(average_comparisons / 3), average_time / 3)
        size *= 2
    return 'EXPERIMENT 4 (REPEATING ARRAY)', execution_result[1], results


def make_graph(exp1: tuple, exp2: tuple, exp3: tuple, exp4: tuple) -> None:
    """
    Make a graph representation of received data
    """
    # TIME GRAPH
    # for EXPERIMENT 1
    x1 = exp1[2].keys()
    y1 = []
    for i in x1:
        y1.append(exp1[2][i][1])
    plt.plot(x1, y1, label=exp1[1])

    # for EXPERIMENT 2
    x2 = exp2[2].keys()
    y2 = []
    for k in x2:
        y2.append(exp2[2][k][1])
    plt.plot(x2, y2, label=exp2[1])

    # for EXPERIMENT 3
    x3 = exp3[2].keys()
    y3 = []
    for m in x3:
        y3.append(exp3[2][m][1])
    plt.plot(x3, y3, label=exp3[1])

    # for EXPERIMENT 4
    x4 = exp4[2].keys()
    y4 = []
    for l in x4:
        y4.append(exp4[2][l][1])
    plt.plot(x4, y4, label=exp4[1])

    plt.xlabel('Array size (power of 2)')
    plt.ylabel('Amount of time (ns)')
    plt.title(exp1[0])

    plt.legend()
    plt.yscale('log')
    plt.savefig(f'TIME - {exp1[0]}.png')
    plt.close()

    # COMPARISONS GRAPH
    # for EXPERIMENT 1
    x1 = exp1[2].keys()
    y1 = []
    for i in x1:
        y1.append(exp1[2][i][0])
    plt.plot(x1, y1, label=exp1[1])

    # for EXPERIMENT 2
    x2 = exp2[2].keys()
    y2 = []
    for k in x2:
        y2.append(exp2[2][k][0])
    plt.plot(x2, y2, label=exp2[1])

    # for EXPERIMENT 3
    x3 = exp3[2].keys()
    y3 = []
    for m in x3:
        y3.append(exp3[2][m][0])
    plt.plot(x3, y3, label=exp3[1])

    # for EXPERIMENT 4
    x4 = exp4[2].keys()
    y4 = []
    for l in x4:
        y4.append(exp4[2][l][0])
    plt.plot(x4, y4, label=exp4[1])

    plt.xlabel('Array size (power of 2)')
    plt.ylabel("No. of comparisons")
    plt.title(exp1[0])

    plt.legend()
    plt.yscale('log')
    plt.savefig(f'COMP - {exp1[0]}.png')
    plt.close()


def testing():
    """
    Runnung necessary tests to check algorithms efficiency
    """
    print("\n===  Testing started  ===\n")

    print("* Running experiment 1 (random array)\n")
    make_graph(test_case_1(
        selection_sort), test_case_1(insertion_sort), test_case_1(shell_sort), test_case_1(merge_sort))

    print("! Finished experiment 1 (random array)\n\n* Running experiment 2 (sorted array)\n")
    make_graph(test_case_2(
        selection_sort), test_case_2(insertion_sort), test_case_2(shell_sort), test_case_2(merge_sort))

    print("! Finished experiment 2 (sorted array)\n\n* Running experiment 3 (reversed array)\n")
    make_graph(test_case_3(
        selection_sort), test_case_3(insertion_sort), test_case_3(shell_sort), test_case_3(merge_sort))

    print("! Finished experiment 3 (sorted array)\n\n* Running experiment 4 (repeating array)\n")
    make_graph(test_case_4(
        selection_sort), test_case_4(insertion_sort), test_case_4(shell_sort), test_case_4(merge_sort))

    print("\nDone.\n")


if __name__ == "__main__":
    testing()
