from Bio import SeqIO


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
    return complement_dna_set


def get_lr_site(sequence):
    record_palindrome = {}
    for i in range(4, 13):
        current_index = 0
        while current_index + i <= len(sequence):
            dna_string = sequence[current_index:current_index + i]
            # print({dna_string:complement(dna_string)})
            # print(dna_string)
            dna_reverse_complement = complement(dna_string)[::-1]
            if dna_string == dna_reverse_complement:
                record_palindrome[current_index + 1] = len(dna_string)
            current_index = current_index + 1

    record_palindrome = {k: v for k, v in sorted(list(record_palindrome.items()))}
    with open("bio_output.txt", "w") as file:
        for k, v in record_palindrome.items():
            print(str(k) + "\t" + str(v))
            file.write(str(k) + "\t" + str(v) + "\n")


if __name__ == '__main__':
    sequence = ""
    for records in SeqIO.parse("Dna Dataset/rosalind_revp.txt", "fasta"):
        sequence = records.seq
    get_lr_site(sequence)
