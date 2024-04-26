#!/bin/bash
# This script sends a POST request to a specified URL and displays the response body
# Usage: ./5-post_params.sh <URL>

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1
EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"

curl -s -X POST "$URL" -d "email=$EMAIL&subject=$SUBJECT"

