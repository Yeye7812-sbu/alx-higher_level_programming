#!/usr/bin/python3

def print_sorted_dictionary(my_dict):
    for g in sorted(my_dict.keys()):
        print("{}: {}".format(g, my_dict[g]))
