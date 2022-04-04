import itertools
permutation_data = []

with open('Dna Dataset/rosalind_perm.txt') as file:
    data = list([int(i) for i in file.readline().splitlines()])

for i in data:
    permutation_data.append(itertools.permutations(range(1, i + 1), i))

for permutation_seq in list(permutation_data):
    perm_seq_list = list(permutation_seq)
    print(len(perm_seq_list))
    for perm_seq in perm_seq_list:
        print(' '.join(str(seq_int) for seq_int in perm_seq), end='\n')
