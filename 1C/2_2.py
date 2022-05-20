#!python3

import sys
import itertools

# A^2 & T^2
# (A + b)^2       = T^2 + b^2
# A^2 + 2Ab + b^2 = T^2 + b^2
# A^2 + 2Ab       = T^2
#       2Ab       = (T^2 - A^2)
#         b       = (T^2 - A^2)/2A

# (A + b1 + b2)^2               = (T^2 + b1^2) + b2^2
# (A + b1)^2 + 2(A+b1)b2 + b2^2 = (T^2 + b1^2) + b2^2
# (A + b1)^2 + 2(A+b1)b2        = (T^2 + b1^2)
#              2(A+b1)b2        = (T^2 + b1^2) - (A + b1)^2
#                     b2        = (T^2 + b1^2) - (A + b1)^2 / 2(A+b1)


T = int(input())
# T = 4

for t in range(1, T+1):
    (N, K) = input().split(' ')
    (N, K) = (int(N), int(K))
    # print(N, K)

    Z =  input().split(' ')

    quit = False
    k = 0
    K_new = []

    while not quit and k <= K:
        print(Z)
        A = 0
        T_s = 0
        for z in Z:
            z_i = int(z)
            A = A + z_i
            T_s = T_s + (z_i * z_i)
        A_s = A * A
        # print(A_s)
        # print(T_s)

        if (T_s - A_s) == 0:
            b = 0
            quit = True
        else:
            if A == 0:
                b = 'IMPOSSIBLE'
                quit = True
            else:
                b = (T_s - A_s) / (2 * A)
                if b == int(b):
                    b = int(b)
                    k = k + 1
                    K_new.append(str(b))
                    quit = True
                    break
                else:
                    # b = 'IMPOSSIBLE'
                    b = int(b)
                    Z.append(str(b))
                    K_new.append(str(b))
                    k = k + 1

    print("Case #{}: {}".format(t, ' '.join(K_new)))
