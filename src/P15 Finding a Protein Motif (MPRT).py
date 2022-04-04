import re, urllib3, certifi
from Bio import SeqIO
from datetime import datetime


def uniprot(uniprot_ids):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    file = open("Dna Dataset/protein_data.txt", "wb")
    file.truncate()
    for id in uniprot_ids:
        url = "https://www.uniprot.org/uniprot/" + id + ".fasta"
        req_data = http.request("GET", url)
        data = req_data.data
        file.write(data)
    file.close()


def protein_motif(uniprot_ids):
    # motif_pattern = re.compile("[N][^P][ST][^P]")  # this is for non overlapping
    motif_pattern = re.compile(r'(?=(N[^P][ST][^P]))')  # this is for  overlapping

    # motif_pattern = re.compile("[N][^P](?:S|T)[^P]")
    motif_dic = {}
    count = 0
    for records in SeqIO.parse("Dna Dataset/protein_data.txt", "fasta"):
        motif_pos = []
        for i in re.finditer(motif_pattern, str(records.seq)):
            motif_pos.append(str(i.start() + 1))
        motif_dic[uniprot_ids[count]] = motif_pos
        count += 1
    return motif_dic


start = datetime.now()
uniprot_ids = []
id = open("Dna Dataset/rosalind_mprt.txt").readlines()
# id = open("dna_sample/mprt.txt").readlines()
for i in id:
    uniprot_ids.append(" ".join(i.split()))
uniprot(uniprot_ids)
motif_dic = protein_motif(uniprot_ids)

for i in uniprot_ids:
    if i in motif_dic.keys():
        if motif_dic[i]:
            print(i)
            print(" ".join(motif_dic[i]))

end = datetime.now()
time_taken = end - start
print('Time: ', time_taken)
