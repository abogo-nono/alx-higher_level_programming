#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp_list = []
    tmp_list += my_list
    if 0 <= idx <= len(tmp_list) - 1:
        tmp_list[idx] = element
    return tmp_list
