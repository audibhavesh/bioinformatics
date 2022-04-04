from Bio import SeqIO
import numpy as np

dna_matrix = []
count = 0


def print_output(profile):
    look_for = ["A", "C", "G", "T"]
    cons = ''
    for i in profile_mat.transpose():
        index = i.tolist().index(max(i.tolist()))
        cons = cons + look_for[index]
    print(cons)
    for i in range(4):
        print(look_for[i] + ": " + ' '.join(map(str, profile_mat[i].tolist())))


for records in SeqIO.parse("Dna Dataset/rosalind_cons.txt","fasta"):
    dna_set = []
    for i in range(len(records.seq)):
        dna_set.append(records.seq[i])
    dna_matrix.append(dna_set)
    del dna_set

seqmat = np.asarray(dna_matrix).transpose()
temp_profile = []
look_for = ["A", "C", "G", "T"]
for i in seqmat:
    elem_count = []
    for ch in look_for:
        Output = np.sum(np.char.count(i, ch))
        elem_count.append(Output)
    temp_profile.append(elem_count)

profile_mat = np.asarray(temp_profile).transpose()
print_output(profile_mat)
