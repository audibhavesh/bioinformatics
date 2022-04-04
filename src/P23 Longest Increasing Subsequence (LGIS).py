import itertools


def lgis(X, compare_func):
    piles = []

    for i in X:
        try:
            idx = next(j for j in range(len(piles)) if compare_func(piles[j][-1][0], i))
            piles[idx].append((i, len(piles[idx - 1]) if idx > 0 else -1))
        except StopIteration:
            piles.append([(i, len(piles[-1]) if piles else -1)])

    result = []
    bp = -1
    for i in range(len(piles) - 1, -1, -1):
        result.append(piles[i][bp][0])
        bp = piles[i][bp][1] - 1

    return result[::-1]


def increasing(seq):
    P = [None] * len(seq)
    M = [None] * len(seq)

    L = 1
    M[0] = 0
    for i in range(1, len(seq)):
        lo = 0
        hi = L
        if seq[M[hi - 1]] < seq[i]:
            j = hi
        else:
            while hi - lo > 1:
                mid = (hi + lo) // 2
                if seq[M[mid - 1]] < seq[i]:
                    lo = mid
                else:
                    hi = mid

            j = lo
        P[i] = M[j - 1]
        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j + 1)

    result = []
    pos = M[L - 1]
    for k in range(L):
        result.append(seq[pos])
        pos = P[pos]

    lis = " ".join([str(i) for i in result[::-1]])
    return lis
    # return (result[::-1])


def decreasing(seq):
    P = [None] * len(seq)
    M = [None] * len(seq)
    L = 1
    M[0] = 0
    for i in range(1, len(seq)):
        lo = 0
        hi = L
        if seq[M[hi - 1]] > seq[i]:
            j = hi
        else:
            while hi - lo > 1:
                mid = (hi + lo) // 2
                if seq[M[mid - 1]] > seq[i]:
                    lo = mid
                else:
                    hi = mid

            j = lo
        P[i] = M[j - 1]
        if j == L or seq[i] > seq[M[j]]:
            M[j] = i
            L = max(L, j + 1)

    result = []
    pos = M[L - 1]
    for k in range(L):
        result.append(seq[pos])
        pos = P[pos]

    lds = " ".join([str(i) for i in result[::-1]])
    return lds


def get_lis(perm_pi):
    lis = ""
    lowest_number = sorted(perm_pi)[0]
    lowest_number_index = perm_pi.index(lowest_number)
    if len(perm_pi) <= 2:
        return perm_pi
    seq = []
    subseq = []
    ind = 0
    for i in range(0, len(perm_pi)):
        print(i)
        if len(subseq) == 0:
            subseq.append([perm_pi[i]])
        else:
            # max_number = max(subseq)
            # print(max_number)
            # print(str(i) + " " + subseq.__str__())
            for index in range(len(subseq)):
                min_value = min(subseq[index])
                max_value = max(subseq[index])
                if min_value == max_value and max_value < perm_pi[i]:
                    try:
                        del subseq[subseq.index([perm_pi[i]])]
                        subseq[index].append(perm_pi[i])
                    except ValueError:
                        subseq[index].append(perm_pi[i])
                elif min_value < perm_pi[i] < max_value:
                    seq_values = [seq_data for seq_data in subseq[index] if seq_data < perm_pi[i]]
                    seq_values.append(perm_pi[i])
                    try:
                        del subseq[subseq.index(seq_values)]
                    # print(seq_values)
                    except ValueError:
                        subseq.append(seq_values)
                elif min_value > perm_pi[i] and max_value > perm_pi[i]:
                    # print(perm_pi[i])
                    try:
                        del subseq[subseq.index([perm_pi[i]])]
                    except ValueError:
                        subseq.append([perm_pi[i]])
                else:
                    subseq[index].append(perm_pi[i])

    print(subseq)
    seq = max(subseq, key=len)
    lis = " ".join([str(i) for i in seq])
    return lis


def get_lds(perm_pi):
    lds = ""
    highest_number = sorted(perm_pi, reverse=True)[0]
    highest_number_index = perm_pi.index(highest_number)
    if len(perm_pi) <= 2:
        return perm_pi
    seq = []
    subseq = []
    for i in range(0, len(perm_pi)):
        if len(subseq) == 0:
            subseq.append([perm_pi[i]])
        else:
            # max_number = max(subseq)
            # print(max_number)
            for seq_index in range(len(subseq)):
                # print(str(i) + " " + subseq.__str__())
                max_number = max(subseq[seq_index])
                min_number = min(subseq[seq_index])
                if min_number == max_number and max_number > perm_pi[i]:
                    subseq[seq_index].append(perm_pi[i])
                elif max_number < perm_pi[i] and min_number < perm_pi[i]:
                    subseq.append(list([perm_pi[i]]))
                elif min_number > perm_pi[i] > max_number:
                    new_seq = []
                    num = subseq[seq_index][0]
                    ind = 0
                    while num > perm_pi[i]:
                        new_seq.append(num)
                        ind += 1
                        num = subseq[seq_index][ind]
                    new_seq.append(perm_pi[i])
                    subseq.append(list(new_seq))
                # elif max_number < perm_pi[i]:
                else:
                    subseq[seq_index].append(perm_pi[i])

    print(subseq)
    seq = max(subseq, key=len)
    lds = " ".join([str(i) for i in seq])
    return lds


def lgis3(seq, count):
    # list of lists of decreasing subsequences
    piles = []

    # all possible indices that could be used for decreasing subsequences
    #    -- i.e. if whole sequence is increasing
    pile_indices = range(count)

    # loop appends each item to the end of first 'pile' for which it continues
    #        the descending subsequence
    #    the second value in each tuple is the index + 1 of the preceeding
    #        pile's last element (or -1 if no preceeding pile)
    #    this allows the traceback to find the last element from the
    #        preceeding pile that was added before this element
    for item in seq:
        # using for & break is simpler and faster than the original
        # elminating xrange(len(piles)) and catching the exception when going
        #    beyond the end of the list (instead of using else) gives an
        #    additional slight improvement in speed
        try:
            for j in pile_indices:

                if piles[j][-1][0] > item:
                    # pile index
                    idx = j

                    # append tuple comprising the current item and the position
                    #   of the preceeding pile's last element (for traceback)
                    piles[idx].append(
                        (
                            item,
                            len(piles[idx - 1]) if idx > 0 else -1
                        )
                    )

                    # resume outer loop
                    break

        except:
            # start a new pile each time the current element is larger than the
            #    last element of all current piles
            piles.append(
                [(
                    item,
                    len(piles[-1]) if piles else -1
                )]
            )

    # the increasing subsequence (reversed)
    result = []

    # backward pointer -- index of last item in the preceeding pile that was
    #    added before the current item
    point_back = -1
    print(piles)
    # reverse iteration over the piles
    for i in range(len(piles) - 1, -1, -1):
        result.append(piles[i][point_back][0])
        point_back = piles[i][point_back][1] - 1

    return result[::-1]


if __name__ == '__main__':
    with open("../Dna Dataset/rosalind_lgis.txt") as file:
        data = file.readlines()
    perm_number = int(data[0].replace("\n", ""))
    perm_pi = [int(i) for i in data[1].replace("\n", "").split(" ")]
    perm_pi = perm_pi[:10]
    # perm_pi = [5, 1, 4, 2, 3]
    # perm_number = 5
    # perm_incr = get_lis(perm_pi)
    # perm_decr = get_lds(perm_pi)
    # print("own")
    # print(perm_incr)
    # print(perm_decr)
    perm_incr2 = increasing(perm_pi)
    # perm_decr2 = decreasing(perm_pi)
    perm_incr3 = lgis3(perm_pi, perm_number)
    # print(lgis(perm_pi, lambda a,b: a < b))
    print("web")
    print(perm_incr2)
    print(" ".join([str(i) for i in perm_incr3]))
    # print(perm_decr2)
    #
    # print("check")
    # print(perm_incr == perm_incr2)
    # print(perm_decr == perm_decr2)
    # BioOutput.__save_output_file__(
    #     data=perm_incr + "\n" + perm_decr,
    #     filename="lgis")
    # for i in range(1, perm_number + 1):
    #     permutations = [i for i in itertools.permutations(perm_pi, i)]
    #     perm_dict[i] = permutations
    #
    # increasing
    # for i, v in perm_dict.items():
    #     perm_value = sorted(v)[-1]
    #     print(perm_value)
