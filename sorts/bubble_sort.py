'''
@__date__ = 2020.02.29
@author = DeLi
'''

import time


def bubble_sort(a_list):
    """
    Pure implementation of bubble sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous

    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> bubble_sort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort([])
    []
    >>> bubble_sort([-23, 0, 6, -4, 34])
    [-23, -4, 0, 6, 34]
    >>> bubble_sort([-23, 0, 6, -4, 34]) == sorted([-23, 0, 6, -4, 34])
    True

    """
    list_length = len(a_list)

    for i in range(list_length-1):
        swapped = False
        for j in range(list_length-1-i):
            if a_list[j] > a_list[j+1]:
                swapped = True
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
                # Show the sorting process
                # print(a_list)
        if not swapped:
            break  # Stop iteration if the collection is sorted.

    return a_list


if __name__ == "__main__":

    start = time.process_time()
    print(bubble_sort([3, 6, 7, 1]))
    print(f"Processing time: {time.process_time() - start}")
