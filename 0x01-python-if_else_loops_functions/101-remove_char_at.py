#!/usr/bin/python3
def remove _char_at(str, n):
    newstr = ""
    for i, c in enumerate(str):
        if i == c:
            continue
        newstr += c
    return newstr
