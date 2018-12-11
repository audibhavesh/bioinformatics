from Bio import motifs,SeqIO
def FSM(dna_set1,dna_set2):
    match=""
    lcms=[]
    print len("".join(dna_set2))
    for i in range(len("".join(dna_set2))):
        if dna_set1[i]==dna_set2[i]:
            match+=dna_set2[i]
        else:
            if len(match)>=3:
                lcms.append(match)
            match=""
    return lcms


dna_set=[]
record=[]
for records in SeqIO.parse("rosalind_lcsm.txt","fasta"):
        dna_set.append(list((records.seq)))
print len(dna_set[1])
freq={}
comb=FSM(dna_set[0],dna_set[1])
for i in dna_set:
    for j in comb:
        if j in "".join(i):
            freq[j] = freq.get(j,0)+1
print max(freq.keys(),key=len)
print freq
# s=[s for s,v in freq.items() if v==max(freq.values())]
# print s
