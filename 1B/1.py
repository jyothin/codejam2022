#!python3

import sys
import itertools

def get_c(d):
    c = 0
    max_i = 0
    while len(d) != 0:
        i = d.pop(0)
        if int(i) >= max_i:
            max_i = int(i)
            c = c + 1
    return c

def get_Ds(D, l, r):
    if l == r:
        return [D[l]]
    return [D[l]]  + get_Ds(D, l + 1, r)
    # return D[r] + get_Ds(D, l, r - 1)

T = int(input())
T = 2

for t in range(1, T+1):
    N = int(input())
    D = input()

    D = D.split(' ')
    
    # Ds = itertools.permutations(D)
    Ds = get_Ds(D, 0, len(D) - 1)
    print(Ds)

    max_c = 0

    for d in Ds:
        print(d)
        new_c = get_c(d)
        print("\tnew_c = {}".format(new_c))
        if new_c > max_c:
            max_c = new_c
        print("\tmax_c = {}".format(max_c))

    print("Case #{}: {}".format(t, max_c))