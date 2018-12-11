def pointmutation(dna_set1,dna_set2):
    count=0
    for i in range(0,len(dna_set1)):
        if(dna_set1[i]!=dna_set2[i]):
            count+=1
    return count

dna_set1=open("Dna Dataset/rosalind_hamm.txt","r").readlines()
print(pointmutation(dna_set1[0],dna_set1[1]))