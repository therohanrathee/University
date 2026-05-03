import time
import matplotlib.pyplot as plt
import tracemalloc


# O(1)
def constant_fun(a):
    return a[0]


# O(n)
def linear_fun(a):
    total = 0
    for x in a:
        total = total + x
    return total


# O(n^2)
def quadratic_fun(a):
    s = 0
    for i in a:
        for j in a:
            s = s + i + j
    return s


# O(log n)
def log_fun(n):
    while n > 1:
        n = n // 2


# Function to check memory
def memory_check(fun, arg):
    tracemalloc.start()
    fun(arg)
    cur, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024


sizes = [10, 100, 500, 1000]

t_const = []
t_lin = []
t_quad = []
t_log = []

m_const = []
m_lin = []
m_quad = []
m_log = []

for n in sizes:

    arr = list(range(n))

    # Constant
    start = time.time()
    constant_fun(arr)
    t_const.append(time.time() - start)
    m_const.append(memory_check(constant_fun, arr))

    # Linear
    start = time.time()
    linear_fun(arr)
    t_lin.append(time.time() - start)
    m_lin.append(memory_check(linear_fun, arr))

    # Quadratic
    start = time.time()
    quadratic_fun(arr)
    t_quad.append(time.time() - start)
    m_quad.append(memory_check(quadratic_fun, arr))

    # Logarithmic
    start = time.time()
    log_fun(n)
    t_log.append(time.time() - start)
    m_log.append(memory_check(log_fun, n))


# Time Graph
plt.figure()
plt.plot(sizes, t_const, label="O(1)")
plt.plot(sizes, t_lin, label="O(n)")
plt.plot(sizes, t_quad, label="O(n^2)")
plt.plot(sizes, t_log, label="O(log n)")
plt.xlabel("Input Size")
plt.ylabel("Time")
plt.title("Time Complexity Comparison")
plt.legend()
plt.show()


# Memory Graph
plt.figure()
plt.plot(sizes, m_const, label="O(1)")
plt.plot(sizes, m_lin, label="O(n)")
plt.plot(sizes, m_quad, label="O(n^2)")
plt.plot(sizes, m_log, label="O(log n)")
plt.xlabel("Input Size")
plt.ylabel("Memory (KB)")
plt.title("Space Complexity Comparison")
plt.legend()
plt.show()