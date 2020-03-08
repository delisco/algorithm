'''
@__date__ = 2020.03.08
@author = DeLi
'''

import time


def fibonacci(n):
    """
    >>> [recur_fibo(i) for i in range(12)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """

    if n < 0:
        print(f'Input incorrect number')
    elif n == 0:
        return 0
    elif n == 1 or n ==2:
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))


if __name__ == "__main__":

    start = time.process_time()
    print(fibonacci(10))
    print(f"Processing time: {time.process_time() - start}")
