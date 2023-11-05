#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    listcopy = my_list.copy()
    listcopy.sort()
    return listcopy[-1]
