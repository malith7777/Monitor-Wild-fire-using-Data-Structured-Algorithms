from Heap import DSAHeapEntry
from Heap import DSAHeap

class DSAHeapEntry:
    def __init__(self, value):
        self.value = value

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l].value > arr[largest].value:
        largest = l

    if r < n and arr[r].value > arr[largest].value:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

