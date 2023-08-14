#!/usr/bin/python3
# 1-element_at.py

def element_at(my_list, idx):
    """ retrieves an element from a list"""
    for my in range(len(my_list)):
        if idx == my:
            print("Element at index {:d} is {}".format(idx, (my_list[my])))
            return (my_list[my])
    if idx < 0 or idx > my:
        return none
