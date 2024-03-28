#!/bin/bash
# request to 0.0.0.0:5000/catch_me that causes the server message containing You got me!
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
