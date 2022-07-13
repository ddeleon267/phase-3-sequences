#!/usr/bin/env python3
import ipdb

def print_fibonacci(length):
    i = 0
    sequence = []

    while i < length:
        # ipdb.set_trace()
        if i == 0 or i == 1:
            sequence.append(i)  
        else: 
            sequence.append(sequence[i - 1] + sequence[i - 2])
        i += 1

    for el in sequence:
        print(el)
# print_fibonacci(9)