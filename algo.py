# Algo 1
# T.C. - O(n*log(log(n)))
def sieveoferatosthenes(n):
    output = []

    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            output.append(p)

    return output


def algov1(a, b):
    genPrime = sieveoferatosthenes(b)
    output = []
    if a == 1:
        output.insert(0, 1)

    for i in range(a, b + 1):
        if i in genPrime:
            output.append(i)
    return output


# Algo 2
# T.C. -  O(sqrt(n))
def isPrimev2(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def algov2(a, b):
    output = []
    for i in range(a, b + 1):
        if isPrimev2(i):
            output.append(i)
    return output


# Algo 3
# T.C. - O(n)
def isPrimev3(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def algov3(a, b):
    output = []
    for i in range(a, b + 1):
        if isPrimev3(i):
            output.append(i)
    return output
