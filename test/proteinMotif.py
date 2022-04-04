from Bio import SeqIO
import exrex
import requests
from io import StringIO

protein_Seq = """MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQ
KDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSS
NEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVN
FKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKY
LNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYD
LSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILM
DLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIY
CLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK""".upper()
protein_Seq2 = """MRASRPVVHPVEAPPPAALAVAAAAVAVEAGVGAGGGAAAHGGENAQPRGVRMKDPPGAP
GTPGGLGLRLVQAFFAAAALAVMASTDDFPSVSAFCYLVAAAILQCLWSLSLAVVDIYAL
LVKRSLRNPQAVCIFTIGDGITGTLTLGAACASAGITVLIGNDLNICANNHCASFETATA
MAFISWFALAPSCVLNFWSMASR"""


def findmotif(protein_seq):
    for prot in range(len(protein_seq)):
        felem = protein_Seq[prot]
        if felem == "N":
            if protein_Seq[prot + 1] != "P":
                if protein_Seq[prot + 2] == "S" or protein_Seq[prot + 2] == "T":
                    if protein_Seq[prot + 3] != "P":
                        print(prot, end=" ")


# id = list(exrex.generate('[A-N,R-Z][0-9][A-Z][A-Z,0-9][A-Z,0-9][0-9]'))[:15]
# print(id)
link = "http://www.uniprot.org/uniprot/{}.fasta".format("B5ZC00")
data = requests.get(link).text
fasta_iterator = SeqIO.parse(StringIO(data), "fasta")
protein_Seq3 = fasta_iterator.__next__().seq
findmotif(protein_Seq3)
