#!python3

import sys

T = int(input())
# T = 1

for i in range(1, T+1):
    N = int(input())
    S = [int(s) for s in input().split(" ")]
    
    l = 0
    d = 0
    while len(S) != 0:
        min_S = min(S)
        min_index = S.index(min_S)

        if min_index != 0:
            S[0], S[min_index] = S[min_index], S[0]

        d = S.pop(0)
        # d = S[0:1][0]
        # S = S[1:]

        l = l + 1

        if l <= d:
            # print("consumed d = %d to get l = %d" %(d, l))
            continue
        else:
            l = l - 1
            # print("consumed d = %d and discarded" %d)

    print("Case #{}: {}".format(i, l))
