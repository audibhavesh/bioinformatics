from itertools import product

from bio_output.output import BioOutput

if __name__ == '__main__':
    with open("../Dna Dataset/rosalind_lexf.txt") as file:
        data = file.readlines()
    lex_string = data[0].replace("\n", "").split(" ")
    comb_number = int(data[1].replace("\n", ""))
    #
    # lex_string = "A C G T".split()
    # comb_number = 2
    pattern = [i for i in map("".join, product(lex_string, repeat=comb_number))]
    BioOutput.__save_output_file__("\n".join(pattern), "lexf")
    print("\n".join(pattern))
