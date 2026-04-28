import time
import matplotlib.pyplot as plt
import tracemalloc


# Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


# Recursive Fibonacci
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


# Fibonacci using DP
def fib_dp(n):

    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


# Memory Check
def mem_check(func, arg):

    tracemalloc.start()

    func(arg)

    cur, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return peak / 1024


values = [5, 7, 9, 11, 13, 15]

fact_time = []
fib_rec_time = []
fib_dp_time = []

fact_mem = []
fib_rec_mem = []
fib_dp_mem = []

for n in values:

    start = time.time()
    factorial(n)
    fact_time.append(time.time() - start)
    fact_mem.append(mem_check(factorial, n))

    start = time.time()
    fib_recursive(n)
    fib_rec_time.append(time.time() - start)
    fib_rec_mem.append(mem_check(fib_recursive, n))

    start = time.time()
    fib_dp(n)
    fib_dp_time.append(time.time() - start)
    fib_dp_mem.append(mem_check(fib_dp, n))


plt.figure()
plt.plot(values, fact_time, label="Factorial")
plt.plot(values, fib_rec_time, label="Recursive Fibonacci")
plt.plot(values, fib_dp_time, label="DP Fibonacci")
plt.title("Time Complexity Comparison")
plt.xlabel("n")
plt.ylabel("Time")
plt.legend()
plt.show()


plt.figure()
plt.plot(values, fact_mem, label="Factorial")
plt.plot(values, fib_rec_mem, label="Recursive Fibonacci")
plt.plot(values, fib_dp_mem, label="DP Fibonacci")
plt.title("Space Complexity Comparison")
plt.xlabel("n")
plt.ylabel("Memory (KB)")
plt.legend()
plt.show()