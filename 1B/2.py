#!python3

import sys
import random

def check(e):
    if e == '-1' or e == -1:
        exit

def r_str():
    return input()

def r_int():
    return int(input())

def fs():
    ps("\n")
    sys.stdout.flush()

def fe():
    pe("\n")
    sys.stderr.flush()

def ps(s):
    sys.stdout.write(str(s))

def pe(s):
    sys.stderr.write(str(s))

def getA(N):
    L = []
    for i in range(0, N):
        r = random.randint(1, 1000000000)
        L.append(r)
    return L

def getB(I):
    L = []
    for i in I:
        L.append(int(i))
    return L

def solution(A, B):
    return A

T = r_int()
# pe(T)
# fe()
t = 1
while t <= T:
    pe("t = {}".format(t))
    fe()

    n = 0
    N = r_int()
    check(N)
    # pe(N)
    # fe()

    # write A
    A = getA(N)
    a = ' '.join(str(a) for a in A)
    ps(a)
    fs()

    # read B
    B = r_str()
    check(B)
    B = B.split(" ")
    B = getB(B)

    # write solution
    C = solution(A, B)
    C = ' '.join(str(c) for c in A)
    ps(C)
    fs()

    t = t + 1

# r = r_str()
# check(r)
# if r == 'CORRECT' or r == 'Wrong answer':
#     pe(r)
#     fe()

# exit()