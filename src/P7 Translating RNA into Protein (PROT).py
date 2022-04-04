def RnatoProtein(dna_set, rna_codon):
    protein = ""
    a = ""
    count = 0
    for i in range(0, len(dna_set)):
        if count < 3:
            a += dna_set[i]
            count += 1
        if count == 3:
            if rna_codon[a] == "STOP":
                break
            elif a in rna_codon:
                protein += rna_codon[a]
            count = 0
            a = ""
    print(protein)


rna_codon = {'ACC': 'T', 'GUC': 'V', 'ACA': 'T', 'ACG': 'T',
             'GUU': 'V', 'AAC': 'N', 'CCU': 'P', 'UAU': 'Y',
             'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N',
             'AGU': 'S', 'ACU': 'T', 'GUG': 'V', 'CAC': 'H',
             'AAA': 'K', 'CCG': 'P', 'CCA': 'P', 'CAA': 'Q',
             'CCC': 'P', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A',
             'UGC': 'C', 'CAG': 'Q', 'UGA': 'STOP', 'UGG': 'W',
             'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G',
             'UCC': 'S', 'UCA': 'S', 'GAA': 'E', 'UAA': 'STOP',
             'UAC': 'Y', 'CGU': 'R', 'UAG': 'STOP', 'AUA': 'I',
             'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'CUG': 'L',
             'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A',
             'AAG': 'K', 'GAU': 'D', 'GGA': 'G', 'UUU': 'F', 'GAC': 'D',
             'GUA': 'V', 'CGA': 'R', 'GCU': 'A', 'UGU': 'C', 'AUU': 'I',
             'UUG': 'L', 'UUA': 'L', 'CGC': 'R', 'UUC': 'F'}

dna_set = open("Dna Dataset/rosalind_prot.txt", "r").read()
RnatoProtein(dna_set, rna_codon)
