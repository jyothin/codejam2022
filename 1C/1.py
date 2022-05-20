#!python3

import sys
import itertools

T = int(input())
# T = 1

for t in range(1, T+1):
    N = int(input())
    S =  input()
    S = S.split(' ')
    # print(S)

    Ss = itertools.permutations(S, N)
    for s in Ss:
        s = ''.join(s)
        # print(s)

        D = ''.join(set(s))
        V = []
        for i in range(0, len(s)):
            if s[i] not in V:
                V.append(s[i])
            else:
                if V.pop() == s[i]:
                    V.append(s[i])
                else:
                    break

        if len(D) == len(V):
            l = s
            break
        else:
            l = 'IMPOSSIBLE'

        # print(len(D))
        # print(len(V))

    print("Case #{}: {}".format(t, l))
