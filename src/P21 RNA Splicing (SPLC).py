from Bio import SeqIO

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


def perform_rna_splicing(sequences):
    dna_string = sequences[0]
    sequences.pop(0)
    for intron in sequences:
        dna_string = dna_string.replace(intron, "")
    return dna_string


def transcript(dna_string):
    return str(dna_string).replace('T', 'U')


def rna_to_protein(dna_set):
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
    return protein


if __name__ == '__main__':
    sequence = ""
    sequence_list = []
    for records in SeqIO.parse("../Dna Dataset/rosalind_splc.txt", "fasta"):
        sequence_list.append(str(records.seq))
    processed_sequence = perform_rna_splicing(sequence_list)
    transcribed_sequence = transcript(processed_sequence.upper())
    translated_sequence = rna_to_protein(transcribed_sequence)
    with open("../bio_output/output_splc.txt", "w") as file:
        file.write(translated_sequence)
    print(translated_sequence)
