def RRrelation(n, k):
    m = 0
    c = 1
    rabbits = 0
    for i in range(0, n):
        rabbits = m * k + c
        m = c
        c = rabbits
    print(m)


seq = open("Dna Dataset/rosalind_fib.txt", "r").read()
n = int(seq[0:2])
k = int(seq[2:])
RRrelation(n, k)
