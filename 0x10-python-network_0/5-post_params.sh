#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
curl -sI $1 | grep "Content-Length" | cut -d " " -f2

