from Bio import SeqIO


def seq_comb(s):
    # slist = [s[0]]
    # slist_rev = [s[-1]]
    # for i in range(2, len(s)):
    #     slist.append(s[0:i])
    # for i in range(len(s) - 2, 0, -1):
    #     slist_rev.append(s[i:])
    slist = []
    slist_rev = []
    for i in range(3, len(s)):
        slist.append(s[0:i])
    for i in range(len(s) - 3, 0, -1):
        slist_rev.append(s[i:])
    return slist + slist_rev


def seq_comb2():
    s = "ATTAGACCTG"
    slist = []
    slist_rev = []
    for i in range(3, len(s)):
        slist.append(s[0:i])
    for i in range(len(s) - 3, 0, -1):
        slist_rev.append(s[i:])


def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        for j in range(len2):
            lcs_temp = 0
            match = ''
            while (i + lcs_temp < len1) and (j + lcs_temp < len2) and string1[i + lcs_temp] == string2[j + lcs_temp]:
                match += string2[j + lcs_temp]
                lcs_temp += 1
            if len(match) > len(answer):
                answer = match
    return answer


def LCS(X, Y, m, n):
    maxLength = 0  # stores the max length of LCS
    endingIndex = m  # stores the ending index of LCS in `X`

    # `lookup[i][j]` stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
    lookup = [[0 for x in range(n + 1)] for y in range(m + 1)]

    # fill the lookup table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # if the current character of `X` and `Y` matches
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1

                # update the maximum length and ending index
                if lookup[i][j] > maxLength:
                    maxLength = lookup[i][j]
                    endingIndex = i

    # return longest common substring having length `maxLength`
    return X[endingIndex - maxLength: endingIndex]


def check_if_has(seq_list, ss):
    f = 0
    for i in seq_list:
        if i not in ss:
            f = 1
            break
    return f == 0


def scs2(sequence_list):
    shortest_seq = ""
    sequence_map = []
    for seq_index in range(len(sequence_list)):
        temp_seq_list = sequence_list.copy()
        try:
            del temp_seq_list[:seq_index]
        except Exception as e:
            temp_seq_list.remove(sequence_list[seq_index])
        sequence_map = []
        pseq = sequence_list[seq_index]
        # print(temp_seq_list)
        for sseq in temp_seq_list:
            print(sseq)
            print(pseq)
            common = LCS(pseq, sseq, len(pseq), len(sseq))
            # print(common)
            if sseq.startswith(common):
                unproseq = sseq[len(common):]
                if check_if_has(sequence_list, pseq + unproseq):
                    sequence_map.append(pseq + unproseq)
            elif sseq.endswith(common):
                unproseq = sseq[:len(common)]
                if check_if_has(sequence_list, unproseq + pseq):
                    sequence_map.append(unproseq + pseq)
            break
    print(sequence_map)
    shortest_seq = str(min(sequence_map, key=len))
    return shortest_seq


def scs(sequence_list):
    shortest_seq = ""
    sequence_map = []
    for seq_index in range(len(sequence_list)):
        p_seq_list = seq_comb(sequence_list[seq_index])
        temp_seq_list = sequence_list.copy()
        temp_seq_list.remove(sequence_list[seq_index])
        pseq_map = []
        for pseq in reversed(p_seq_list):
            for sseq in temp_seq_list:
                if sseq.startswith(pseq) or sseq.endswith(pseq):
                    if sseq.startswith(pseq):
                        unproseq = sseq[len(pseq):]
                        pseq_map.append(sequence_list[seq_index] + unproseq)
                    elif sseq.endswith(pseq):
                        unproseq = sseq[:len(pseq)]
                        pseq_map.append(unproseq + sequence_list[seq_index])
            if len(pseq_map) > 0:
                short_seq = min(pseq_map)
                sequence_map.append(short_seq)
                break
    print("seq done")
    sp_map = []
    k = 0
    for i in sequence_map:
        for j in sequence_map:
            print(str(k))
            if i == j:
                continue
            common = LCS(i, j, len(i), len(j))
            # print(common)
            if j.startswith(common):
                unproseq = j[len(common):]
                if check_if_has(sequence_list, i + unproseq):
                    sp_map.append(i + unproseq)
            elif j.endswith(common):
                unproseq = j[:len(common)]
                if check_if_has(sequence_list, unproseq + i):
                    sp_map.append(unproseq + i)
            k += 1
    shortest_seq = str(min(sp_map, key=len))
    return shortest_seq


if __name__ == '__main__':
    sequence = ""
    sequence_list = []
    # seq_comb2()
    for records in SeqIO.parse("../Dna Dataset/rosalind_long.txt", "fasta"):
        sequence_list.append(str(records.seq))
    sequence_list = ["ATTAGACCTG", "CCTGCCGGAA", "AGACCTGCCG", "GCCGGAATAC"]
    shortest_seq = scs2(sequence_list)
    with open("../bio_output/output_long.txt", "w") as file:
        file.write(shortest_seq)
    print(shortest_seq)
