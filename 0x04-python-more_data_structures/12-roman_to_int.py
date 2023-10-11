#!/usr/bin/python3
def factars_user(list_num):
    abudu = 0
    event = max(list_num)

    for n in list_num:
        if event > n:
            abudu += n

    return (event - abudu)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    milan = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(milan.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if milan.get(ch) <= last_rom:
                    num += factars_user(list_num)
                    list_num = [milan.get(ch)]
                else:
                    list_num.append(milan.get(ch))

                last_rom = milan.get(ch)

    num += factars_user(list_num)

    return (num)
