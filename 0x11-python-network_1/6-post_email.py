#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends a POST request
to the passed URL with the email
"""
import requests
import sys


if __name__ == "__main__":
    datas = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(datas.text)
