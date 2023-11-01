#!/usr/bin/python3
for i in range(25, -1, -11):
    c = i + ord('A')
    if i % 2 == 1:
        c += 32
    print("{:d}".format(c), end="")
