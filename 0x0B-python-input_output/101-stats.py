#!/usr/bin/python3
"""module for reading standard input and computes metrics.
"""


def display_state(size, manira_code):
    """function for matrics.

    Args:
        size (int): receiving the size.
        manira_code (dict): receive the count status.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key])

if __name__ == "__main__":
    import sys

    size = 0
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0
    manira_code = {}

    try:
        for line in sys.stdin:
            if count == 10:
                display_state(size, manira_code)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if manira_code.get(line[-2], -1) == -1:
                        manira_code[line[-2]] = 1
                    else:
                        manira_code[line[-2]] += 1
            except IndexError:
                pass

        display_state(size, manira_code)

    except KeyboardInterrupt:
        display_state(size, manira_code)
        raise
