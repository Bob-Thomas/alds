import sys
import threading


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


import random

temp = 0


def badqsort(a, low=None, high=None):
    global temp
    if high is None:
        high = len(a) - 1
    if low is None:
        low = 0
    if low < high:
        b = a[low:high + 1]
        i = b.index(min(b))
        swap(a, low, i + low)
        m = low
        for j in range(low + 1, high + 1):
            if a[j] < a[low]:
                temp += 1
                m += 1
                swap(a, m, j)
                # low < i <= m : a[i] < a[low]
                # i > m        : a[i] >= a[low]
        swap(a, low, m)
        # low <= i < m : a[i] < a[m]
        # i > m              : a[i] >= a[m]
        if m > 0:
            temp += 1
            badqsort(a, low, m - 1)
        badqsort(a, m + 1, high)


def qsort(a, low=0, high=-1):
    global temp
    if high == -1:
        high = len(a) - 1
    if low < high:
        swap(a, low, random.randint(low, high))
        m = low
        for j in range(low + 1, high + 1):
            if a[j] < a[low]:
                m += 1
                swap(a, m, j)
                # low < i <= m : a[i] < a[low]
                # i > m        : a[i] >= a[low]
        swap(a, low, m)
        # low <= i < m : a[i] < a[m]
        # i > m              : a[i] >= a[m]
        if m > 0:
            temp += 1
            qsort(a, low, m - 1)
        qsort(a, m + 1, high)


def isSorted(a):
    i = 0
    while i < len(a) - 1 and a[i] <= a[i + 1]:
        i += 1

    return i == len(a) - 1


if __name__ == '__main__':
    sys.setrecursionlimit(10000000)
    #    import random
    a = [0] * 2000
    for i in range(2000):
        a[i] = random.randint(0, 2000)

    gud = list(a)
    bad = list(a)
    print("Gud qsort")
    print("a gegenereerd")
    print(gud[500:510])
    b = list(gud)

    import timeit

    timer = timeit.default_timer

    t1 = timer()
    qsort(gud)
    print(gud[500:510])
    t2 = timer()
    print(t2 - t1)
    print(isSorted(gud))

    b.sort()
    print(gud == b)

    print(temp)

    temp = 0
    print("Bad qsort")
    print(bad[500:510])
    b = list(bad)

    import timeit

    timer = timeit.default_timer

    t1 = timer()
    badqsort(bad)
    print(bad[500:510])
    t2 = timer()
    print(t2 - t1)
    print(isSorted(bad))

    b.sort()
    print(bad == b)

    print(temp)
