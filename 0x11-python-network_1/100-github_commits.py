#!/usr/bin/python3
"""
School staff evaluates candidates applying for a back-end
position with multiple technical challenges, like this one
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    changes = r.json()
    try:
        for x in range(10):
            print("{}: {}".format(
                changes[x].get("sha"),
                changes[x].get("commit").get("author").get("name")))
    except IndexError:
        pass
