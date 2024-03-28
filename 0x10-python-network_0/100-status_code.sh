#!/bin/bash
#  Bash script that sends a request to a URL passed and displays only the status code of the response.
curl -so /dev/null -w "%{http_code}" "$1"
