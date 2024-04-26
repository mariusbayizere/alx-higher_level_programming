#!/usr/bin/python3
"""
POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    bane = parse.urlencode(values)
    bane = bane.encode('ascii')
    xx = request.Request(sys.argv[1], bane)
    with request.urlopen(xx) as response:
        body = response.read()
        print(body.decode('utf-8'))
