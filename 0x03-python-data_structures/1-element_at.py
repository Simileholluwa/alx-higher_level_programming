#!/usr/bin/python3
def element_at(my_list, idx):
    '''A function that returns an element from a list'''

    if idx < 0:
        return None

    if idx > len(my_list) - 1:
        return None

    return my_list[idx]
