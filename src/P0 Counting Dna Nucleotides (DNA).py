def count_dna(dna_string):
    A = 0
    T = 0
    G = 0
    C = 0
    for i in str(dna_string).upper():
        if 'A' in i:
            A = A + 1
        elif 'T' in i:
            T = T + 1
        elif 'G' in i:
            G = G + 1
        elif 'C' in i:
            C = C + 1
    count = str(A) + " " + str(C) + " " + str(G) + " " + str(T)
    return count


if __name__ == '__main__':
    dna_string = open("../Dna Dataset/rosalind_dna.txt", "r").read()
    print(count_dna(dna_string))
