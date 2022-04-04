import os

order = [
    "DNA",
    "RNA",
    "REVC",
    "FIB",
    "GC",
    "HAMM",
    "IPRB",
    "PROT",
    "SUBS",
    "CONS",
    "FIBD",
    "GRPH",
    "IEV",
    "LCSM",
    "LIA",
    "MPRT",
    "MRNA",
    "ORF",
    "PERM",
    "PRTM",
    "REVP",
    "SPLC",

]
if __name__ == '__main__':
    files = os.listdir("../src")
    for codeIndex in range(0, len(order)):
        code = order[codeIndex]
        code = "(" + code + ")"
        filename = [filename for filename in files if code in filename][0]
        check = filename[0] != "P" and type(int(filename[1])) != int
        if check:
            old_file_path = "../src/" + filename
            print(old_file_path)
            new_file_path = "../src/" + "P" + str(codeIndex) + " " + filename
            print(new_file_path)
            os.rename(old_file_path, new_file_path)
        # break

    # print(files)
