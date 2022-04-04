def Mortalfib(n, m):
    arr = [0 for i in range(m - 1)]
    arr.append(1)
    for gen in range(n - 1):
        newR = sum([arr[i] for i in range(m - 1)])
        for i in range(m - 1):
            arr[i] = arr[i + 1]
        arr[m - 1] = newR
    print(sum(arr))

    # li=[]
    # li.append([1, 2])#[mature,age]
    # for i in range(n-2):
    #     for j in range(len(li)):
    #         if li[j][1]<m:
    #             if li[i][0]==1:
    #                 li.append([0,0])
    #                 li[i][1]+=1
    #             else:
    #                 li[i][0]=1
    #                 li[i][1]=1
    #
    # print len(li)


MFR = open("Dna Dataset/rosalind_fibd.txt", "r").read()
n, m = MFR.split(" ")
Mortalfib(int(n), int(m))
