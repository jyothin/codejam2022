#!python3

import sys

T = input()

def generic_row(C, cell, first, second, separator):
    row = first + second + separator
    for j in range(1, C):
        row = row + cell + separator
    return row

for i in range(1, int(T)+1):
    size = input()
    size = size.split(' ');
    R = int(size[0])
    C = int(size[1])
    print("Case #" + str(i) +":")
    for row_count in range(1, 2*R+1+1):
        if row_count == 1:
            print(generic_row(C, '-', '.', '.', '+'))
            continue
        if row_count == 2:
            print(generic_row(C, '.', '.', '.', '|'))
            continue
        if row_count%2 == 0:
            print(generic_row(C, '.', '|', '.', '|'))
        else:
            print(generic_row(C, '-', '+', '-', '+'))
    