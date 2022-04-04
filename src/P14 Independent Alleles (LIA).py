import math


def comb(n, r):
    return float(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))


def mendals_second_law(k, n):
    ia = 0.0
    N = pow(2, k)
    for i in range(n, N + 1):
        ia += comb(N, i) * pow(0.25, i) * pow(0.75, N - i)
    print(ia)


k, n = dna_set = open("Dna Dataset/rosalind_lia.txt", "r").read().split()
mendals_second_law(int(k), int(n))
