#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    '''A function that replace an element at a specific position'''

    if idx < 0:
        return my_list

    if idx > len(my_list) - 1:
        return my_list

    my_list.pop(idx)
    my_list.insert(idx, element)

    return my_list
