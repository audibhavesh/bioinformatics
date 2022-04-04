import math


def CEO(off):
    prob_off = [1.0, 1.0, 1.0, 0.75, 0.5, 0]
    sum = 0
    for i in range(len(off)):
        sum = sum + 2 * (off[i] * prob_off[i])
    print(sum)


data_set = open("Dna Dataset/rosalind_iev.txt", "r").read()
n = data_set.split(" ")
n = [int(i) for i in n]
CEO(n)
