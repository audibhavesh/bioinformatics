def prt_to_mrna(protein_count, protein_seq):
    total = protein_count['STOP']
    for i in protein_seq:
        total *= protein_count[i]
    print(total % 1000000)


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
             'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M',
             'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R',
             'CUA': 'L', 'GCC': 'A', 'AAG': 'K', 'GAU': 'D',
             'GGA': 'G', 'UUU': 'F', 'GAC': 'D', 'GUA': 'V',
             'CGA': 'R', 'GCU': 'A', 'UGU': 'C', 'AUU': 'I',
             'UUG': 'L', 'UUA': 'L', 'CGC': 'R', 'UUC': 'F'}

protein_seq = list("".join(open("Dna Dataset/rosalind_mrna.txt", "r").read().split()))
protein_count = {}
for i, j in rna_codon.items():
    if j not in protein_count:
        protein_count[j] = 0
    protein_count[j] += 1
prt_to_mrna(protein_count, protein_seq)
