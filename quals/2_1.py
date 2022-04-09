#!python3

import sys
import random

T = input()
# T = 1
def get_weights(c, min_c, m, min_m, y, min_y, k, min_k):
    w = [1.0, 1.0, 1.0, 1.0]
    
    diff_c = abs(c-min_c)
    diff_m = abs(m-min_m)
    diff_y = abs(y-min_y)
    diff_k = abs(k-min_k)

    diff_sum = diff_c + diff_m + diff_y + diff_k

    if diff_sum != 0:
        w[0] = diff_c / diff_sum
        w[1] = diff_m / diff_sum
        w[2] = diff_y / diff_sum
        w[3] = diff_k / diff_sum

    return w

for i in range(1, int(T)+1):
    p1 = input()
    p1 = p1.split(' ')
    p1 = [int(p1[0]), int(p1[1]), int(p1[2]), int(p1[3])]
    # print(p1)
    
    p2 = input()
    p2 = p2.split(' ')
    p2 = [int(p2[0]), int(p2[1]), int(p2[2]), int(p2[3])]
    # print(p2)

    p3 = input()
    p3 = p3.split(' ')
    p3 = [int(p3[0]), int(p3[1]), int(p3[2]), int(p3[3])]
    # print(p3)
    
    min_c = min(p1[0], p2[0], p3[0])
    min_m = min(p1[1], p2[1], p3[1])
    min_y = min(p1[2], p2[2], p3[2])
    min_k = min(p1[3], p2[3], p3[3])
    # print('mins: ')
    # print(min_c, min_m, min_y, min_k)

    possible = True
    sample = 0
    total = 1000000
    converged = False

    sample_size = (min_c if min_c != 0 else 1) + (min_m if min_m != 0 else 1) + (min_y if min_y == 0 else 1) + (min_k if min_k == 0 else 1)
    while (possible and not converged and sample <= 1):
        # print('converged: ' + str(converged))
        # print('sample: ' + str(sample))
        sample = sample + 1
        c = 0 #random.randint(0, min_c)
        m = 0 #random.randint(0, min_m)
        y = 0 #random.randint(0, min_y)
        k = 0 #random.randint(0, min_k)

        if (min_c + min_m + min_y + min_k) < 1000000:
            possible = False

        # (c, m, y, k) = (300000, 200000, 300000, 200000)
        # print('color:')
        # print(c, m, y, k)

        iteration = 0
        delta = 0.0
        diff = 1000000
        iteration_size = sample_size
        while (possible and diff != 0 and iteration <= iteration_size):
            iteration = iteration + 1
            # adjust = True if (diff <= 3 and delta == 0.0) else False
            if diff <= 3 and delta < 1.0:
                adjust = True
            else:
                adjust = False
            # print(diff, delta, adjust)
            if 0 < delta and delta <= 3:
                w = [1.0, 1.0, 1.0, 1.0]
            else:
                w = get_weights(c, min_c, m, min_m, y, min_y, k, min_k)
            # print('%0.2f %0.2f %0.2f %0.2f' %(w[0], w[1], w[2], w[3]))

            if adjust and abs(c-min_c) >= diff:
                c = c + int(w[0] * delta) + diff
                adjust = False
            else:
                c = c + int(w[0] * delta) + 0
            if not (0 <= c and c <= min_c):
                print('c: 0 <= %d <= %d out of bounds ' %(c, min_c))
                break

            if adjust and abs(m-min_m) >= diff:
                m = m + int(w[1] * delta) + diff
                adjust = False
            else:
                m = m + int(w[1] * delta) + 0
            if not (0 <= m and m <= min_m):
                print('m: 0 <= %d <= %d out of bounds' %(m, min_m))
                break

            if adjust and abs(y-min_y) >= diff:
                y = y + int(w[2] * delta) + diff
                adjust = False
            else:
                y = y + int(w[2] * delta) + 0
            if not (0 <= y and y <= min_y):
                print('y: 0 <= %d <= %d out of bounds' %(y, min_y))
                break

            if adjust and abs(k-min_k) >= diff:
                k = k + int(w[3] * delta) + diff
                adjust = False
            else:
                k = k + int(w[3] * delta) + 0
            if not (0 <= k and k <= min_k):
                print('k: 0 <= %d <= %d out of bounds' %(k, min_k))
                break

            diff = total - (c + m + y + k)
            delta = diff/4.0
            # print('%d %d %d %d %0.2f %d %d %d %d %d' %(sample, iteration, diff, diff/4, delta, c, m, y, k, c+m+y+k))

            # for some condition this will become impossible
            if adjust:
                possible = False
            # then set possible=False

        if possible and diff == 0:
            converged = True

    if not converged:
        possible = False

    # print("Case #" + str(i) +": ")
    if possible:
        print("Case #" + str(i) +": %d %d %d %d" %(c, m, y, k))
    else:
        print("Case #" + str(i) +": " + 'IMPOSSIBLE')
    
#    converge to 10
#    2 2 2 2 = 8
#    10-8=2
#    2/4=0.5
#    2.5 2.5 2.5 2.5 = 10

#    3 3 3 3 = 12
#    10-12=-2
#    -2/4=-0.5
#    2.5 2.5 2.5 2.5 = 10
    
#    2 4 1 6 = 13
#    10-13=-3
#    -3/4=-0.75
#    1.25 3.25 0.25 5.25 = 10
    