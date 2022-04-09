#!python3

import sys
import itertools

T = int(input())
# T = 1

for t in range(1, T+1):
    S = input()
    l = []
    l.append(S)

    for i in range(1, len(S)+1):
        h = itertools.combinations(S, i)
        for hl in h:
            hl = list(hl)
            # print(hl)
            s = list(S)
            # print(s)
            sn = ''

            ss = ''
            hll = ''
            # print("{} - {} - {}".format(s, hl, sn))
            while len(s) > 0:
                sn = sn + ss
                if ss == hll:
                    sn = sn + ss
                    hll = hl.pop(0) if len(hl) > 0 else ''
                ss = s.pop(0) if len(s) > 0 else ''            
            sn = sn + ss
            if ss == hll:
                sn = sn + ss
            
            # print(sn)
            # if sn not in l:
            l.append(sn)
        # print(l)
    l.sort()
    print("Case #{}: {}".format(t, l[0]))