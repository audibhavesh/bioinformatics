from Bio import SeqIO
from itertools import combinations


def is_getting_overlaped(seq1, seq2, k):
    return seq1[-k:] == seq2[:k]


def find_overlap(dna_list, k):
    adjacency_list = []
    for set1, set2 in combinations(dna_list, 2):
        dna_seq1, dna_seq2 = dna_list[set1], dna_list[set2]
        if is_getting_overlaped(dna_seq1, dna_seq2, k):
            adjacency_list.append([set1, set2])
        if is_getting_overlaped(dna_seq2, dna_seq1, k):
            adjacency_list.append([set2, set1])

    return adjacency_list


li = {}
for records in SeqIO.parse("Dna Dataset/rosalind_grph.txt", "fasta"):
    li[records.id] = records.seq

output_list=find_overlap(li,3)
print(output_list)
for i in output_list:
    print(' '.join(i))