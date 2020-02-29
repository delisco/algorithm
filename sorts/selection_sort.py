'''
@__date__ = 2020.02.29
@author = DeLi
'''

import time


def selection_sort(a_list):
    """
    Pure implementation of bubble sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous

    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> selection_sort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> selection_sort([])
    []
    >>> selection_sort([-23, 0, 6, -4, 34])
    [-23, -4, 0, 6, 34]
    >>> selection_sort([-23, 0, 6, -4, 34]) == sorted([-23, 0, 6, -4, 34])
    True

    """
    list_length = len(a_list)

    for i in range(list_length-1):
        least = i
        for k in range(i+1, list_length):
            if a_list[k] < a_list[least]:
                least = k
        if least != i:
            a_list[least], a_list[i] = a_list[i], a_list[least]

    return a_list


if __name__ == "__main__":

    start = time.process_time()
    print(selection_sort([0, 5, 2, 3, 2]))
    print(f"Processing time: {time.process_time() - start}")
