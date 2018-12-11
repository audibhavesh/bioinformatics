from Bio import SeqIO
def CP(dna_matrix):
    A,C,G,T=[],[],[],[]
    con=[]
    for i in range(len(dna_matrix)):
        a,c,g,t=0,0,0,0
        for j in range(len(dna_matrix)):
            if dna_matrix[i][j]=='A':
                a+=1
            elif dna_matrix[i][j] == 'C':
                c += 1
            elif dna_matrix[i][j] == 'T':
                t += 1
            elif dna_matrix[i][j] == 'G':
                g += 1
        A.append(str(a))
        C.append(str(c))
        G.append(str(g))
        T.append(str(t))
        k=max(a,c,g,t)
        if k==a:
            con.append("A")
        if k==c:
            con.append("C")
        if k==t:
            con.append("T")
        if k==g:
            con.append("G")

    print "".join(con)
    print "A:"," ".join(A)
    print "C:"," ".join(C)
    print "G:"," ".join(G)
    print "T:"," ".join(T)

dna_matrix=[]
count=0

for records in SeqIO.parse("Dna Dataset/rosalind_cons.txt","fasta"):
    dna_set=[]
    for i in range(len(records.seq)):
        dna_set.append(records.seq[i])
    dna_matrix.append(dna_set)
    del dna_set
CP(dna_matrix)
