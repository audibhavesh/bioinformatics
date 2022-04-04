from Bio import SeqIO


def FSM(dna_set):
    dna_set1 = dna_set[0]
    dna_data_set = dna_set[1:]

    motif = ""
    for i in range(len(dna_set1)):
        for j in range(i, len(dna_set1)):
            check_motif = dna_set1[i:j + 1]
            f = False
            for dna in dna_data_set:
                if check_motif in dna:
                    f = True
                else:
                    f = False
                    break
            if f and len(check_motif) > len(motif):
                motif = check_motif
    print(motif)


dna_set = []

for records in SeqIO.parse("Dna Dataset/rosalind_lcsm.txt", "fasta"):
    dna_set.append(("".join(records.seq)))

FSM(dna_set)
# for i in dna_set:
#     print i
