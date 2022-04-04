from Bio import SeqIO
from fractions import Fraction


def gc(dna_set):
    # g = Fraction(str(dna_set).count("G"))
    # c = Fraction(str(dna_set).count("C"))
    g = dna_set.count("G")
    c = dna_set.count("C")
    totalGC = g + c
    return 100 * (float(totalGC) / len(dna_set))


li = {}
for records in SeqIO.parse("Dna Dataset/rosalind_gc.txt", "fasta"):
    li[records.id] = gc(records.seq)
gc_content = 0
id = ""
for i in li:
    if gc_content < li[i]:
        id = i
        gc_content = li[i]
print(id)
print("%.6f" % gc_content)
