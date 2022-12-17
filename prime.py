import random

def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)
    return prime_list

def randomChoice():
    prime_set = set()
    prime_list = primesInRange(512, 1024)
    while len(prime_set) < 2:
        prime_set.add(random.choice(prime_list))

    result = list(prime_set)
    return result[0], result[1]