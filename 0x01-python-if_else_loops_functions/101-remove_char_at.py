#!/usr/bin/python3
def remove_char_at(ptr, x):
    if x < 0:
        return (ptr)
    return (ptr[:x] + ptr[x+1:])
