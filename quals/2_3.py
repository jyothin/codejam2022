#!python3

import sys

T = int(input())
# T = 1

for i in range(1, T+1):
    p1 = [int(p) for p in input().split(" ")]
    p2 = [int(p) for p in input().split(" ")]
    p3 = [int(p) for p in input().split(" ")]

    min_c = min(p1[0], p2[0], p3[0])
    min_m = min(p1[1], p2[1], p3[1])
    min_y = min(p1[2], p2[2], p3[2])
    min_k = min(p1[3], p2[3], p3[3])

    start = [0, 0, 0, 0]

    remaining = 1000000
    max_list = [min_c, min_m, min_y, min_k]

    while remaining > 0:
        max_now = max(max_list)
        if max_now < remaining:
            index_max = max_list.index(max_now)
            start = start[:index_max]+[max_now]+start[index_max+1:]
            max_list = max_list[:index_max]+[0]+max_list[index_max+1:]
            remaining = remaining - max_now
        else:
            index_max = max_list.index(max_now)
            start = start[:index_max]+[remaining]+start[index_max+1:]
            max_list = max_list[:index_max]+[max_now - remaining]+max_list[index_max+1:]
            remaining = remaining - remaining

        (c, m, y, k) = (start[0], start[1], start[2], start[3])
        if c + m + y + k == 1000000:
            break
        if (c == min_c and m == min_m and y == min_y and k == min_k):
            break

    # if start[0] == 0 and remaining < min_c:
    #     start[0] = remaining
    # elif start[1] == 0 and remaining < min_m:
    #     start[1] = remaining
    # if start[2] == 0 and remaining < min_y:
    #     start[2] = remaining
    # if start[3] == 0 and remaining < min_k:
    #     start[3] = remaining

    # (c, m, y, k) = (start[0], start[1], start[2], start[3])
    # print(c, m, y, k)

    # while (c <= min_c or m <= min_m or y <= min_y or k <= min_k):
    #     if (c == min_c and m == min_m and y == min_y and k == min_k):
    #         break

    #     c = (c + 1) if c < min_c else c
    #     if c + m + y + k == 1000000:
    #          break

    #     m = (m + 1) if m < min_m else m
    #     if c + m + y + k == 1000000:
    #          break

    #     y = (y + 1) if y < min_y else y
    #     if c + m + y + k == 1000000:
    #          break

    #     k = (k + 1) if k < min_k else k 
    #     if c + m + y + k == 1000000:
    #          break

    #     # print(c, m, y, k)

    if (c + m + y + k) == 1000000:
        print("Case #{}: {} {} {} {}".format(i, c, m, y, k))
    else:
        print("Case #{}: {}".format(i, "IMPOSSIBLE"))
