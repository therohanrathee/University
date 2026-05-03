import time
import matplotlib.pyplot as plt
import tracemalloc


# Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# Binary Search
def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Memory Check
def check_memory(fun, *args):
    tracemalloc.start()
    fun(*args)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024


sizes = [100, 500, 1000, 1500, 2000]

linear_time = []
binary_time = []

linear_mem = []
binary_mem = []

for n in sizes:

    arr = list(range(n))
    target = arr[-1]

    # Linear Search
    start = time.time()
    linear_search(arr, target)
    linear_time.append(time.time() - start)
    linear_mem.append(check_memory(linear_search, arr, target))

    # Binary Search
    start = time.time()
    binary_search(arr, target)
    binary_time.append(time.time() - start)
    binary_mem.append(check_memory(binary_search, arr, target))


# Time Graph
plt.figure()
plt.plot(sizes, linear_time, label="Linear Search")
plt.plot(sizes, binary_time, label="Binary Search")
plt.title("Time Complexity Comparison")
plt.xlabel("Input Size")
plt.ylabel("Time (s)")
plt.legend()
plt.show()


# Memory Graph
plt.figure()
plt.plot(sizes, linear_mem, label="Linear Search")
plt.plot(sizes, binary_mem, label="Binary Search")
plt.title("Space Complexity Comparison")
plt.xlabel("Input Size")
plt.ylabel("Memory (KB)")
plt.legend()
plt.show()