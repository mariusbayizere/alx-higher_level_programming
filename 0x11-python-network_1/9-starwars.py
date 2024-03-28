#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    search = 'https://swapi.co/api/people/?search={}'.format(sys.argv[1])
    xx = requests.get(search)
    pyth = xx.json()
    print("Number of results: {}".format(pyth.get('count')))
    for xxxx in pyth.get('results'):
        print(xxxx.get('name'))
