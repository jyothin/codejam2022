#!python3

import sys
from operator import add

T = int(input())
# T = 1

for i in range(1, T+1):
    N = int(input())
    S_i = [int(s_i) for s_i in input().split(" ")]
    
    # for n in range(0, N):
    #     S[int(S_i[n])-1] = S[int(S_i[n])-1] + 1
    # S.sort()
    S = S_i
    # print(S)

    l = 0
    d = 0
    while len(S) != 0:
        min_S = min(S)
        min_index = S.index(min_S)

        temp = S[0]
        S[0] = S[min_index]
        S[min_index] = temp

        d = S.pop(0)

        l = l + 1

        if l <= d:
            # print("consumed d = %d to get l = %d" %(d, l))
            continue
        else:
            l = l -  1
            # print("consumed d = %d and discarded" %d)

    # if l > d:
    #     l = l - 1

    print("Case #" + str(i) +": %d" %(l))
