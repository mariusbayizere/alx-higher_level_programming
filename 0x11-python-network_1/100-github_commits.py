#!/usr/bin/python3
"""
School staff evaluates candidates applying for a back-end position
with multiple technical challenges
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    x = get(url, auth=auth.HTTPBasicAuth(user, password))
    print(x.json().get('id'))
