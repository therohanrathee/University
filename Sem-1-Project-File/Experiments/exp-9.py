def find_primes(n) :
    primes = []
    for num in range(2, n + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
        if input("Enter 'stop' to break or press Enter to continue: ") == 'stop':
            break
    return primes
n = 10
print(find_primes(n))