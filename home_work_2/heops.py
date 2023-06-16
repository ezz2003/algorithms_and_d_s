from random import randint


def heapify(arr, n, i):
    large = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        large = l
    if r < n and arr[large] < arr[r]:
        large = r
    if large != i:
        arr[i], arr[large] = arr[large], arr[i]
        heapify(arr, n, large)


def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


n = 40
a = [randint(1, 199) for i in range(n)]
print(a)
heapSort(a)
print(a)
