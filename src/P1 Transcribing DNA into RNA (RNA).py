def transcript(dna_string):
    return str(dna_string).replace('T', 'U')


dna_string = "AAGATTGCACGGGACGAACGATTAAATAGTTCTAAGTCATCGCCTGAGAATTATTCCAACGATTTGCCAGGCGCGTTATCAATTCCGGACGCTCTATGATACCGCGCTAATTTGGCATTACGTCATCGTTATGCACCCTGGATAACCAAATTCCGCTGTGGAGGGACAGAGTCAGCTGGCTCGCATTCGAAGGATGCCCTGACGAAGGACTGAAACGTCAACGATAGGCACAACCGTGGACAATTACATTAAGACCTAGGATCCATCGCCTTCGGAGGCCCTATGAAACGTAACGTTCTGGAGCACGTATAGTAATTGGACGTCCCCGATACCTCGAGCGGCACTTCTTCAGTGTAGCAAACGTAAAGTCTTCACCGATCGGCACCGCACGGCTCCGTCACCATGTCAACACACTCATTCCTTCAAGCGGGATACTCTTTCAAGATGTGCCCGGGAAGTTTGGGCGGACATATGAACTCCTTCCGCCGAAGAAATCGGTGAACCAAGAGCTACTCGGCGCCCAAAGGATATGGCGTCTACCGACTTGGTTTACGTAAGCTTATACAACGTCCACCACGCGCGAGCCTGACGGGCTCCGGTAGTGGCCCGTAGAGCCAGCGTGCGACTGATTGAGCTGATCTTTTCACGAGGCTCTCCCTCGGTGGCCTTGCGTGAGTCACTAATCACGGACTCTGCGCGGATAAGCTAGTTGGCCCGCACCTACTTGTCAAAGCGGGTTCCTGTTTAGTACTGGGGCCGTGCGTTTAATGAAACTCTCCGAATCTGAGGCAGTGAGCGTACTACATAGGCTAATCCTTTAACGAAGCTGGTAAAAAGAACGCTCGATTAGAGATGTTACAACTAGCGTCTATCACCGGGAATCTTCTTACCTGGCAGACATTCAGCTAAGACGATGTCGTTGC "

print(transcript(dna_string.upper()))
