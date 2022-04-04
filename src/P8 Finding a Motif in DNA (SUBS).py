def motif(dna_set, motif_dna):
    l = len(motif_dna)
    a = []
    for i in range(0, len(dna_set) - l + 1):
        if dna_set[i:l + i] == motif_dna:
            a.append(str(i + 1))
    print(" ".join(a))


dna_set = open("Dna Dataset/rosalind_subs.txt", "r").readlines()
k = dna_set[1][0:len(dna_set[1]) - 1]
motif(dna_set[0], k)
