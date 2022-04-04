def complement(rev_dna_set):
    complement_dna_set = ""
    for i in rev_dna_set:
        if i == "A":
            complement_dna_set += "T"
        elif i == "G":
            complement_dna_set += "C"
        elif i == "C":
            complement_dna_set += "G"
        elif i == "T":
            complement_dna_set += "A"

    print(complement_dna_set)


dna_set = open("Dna Dataset/rosalind_revc.txt", "r").read()
complement("".join(reversed(dna_set.upper())))
