#!/bin/bash

# Git operations
git add .
git commit -m ":0x0A. Python - Inheritance"
git push

# Send email
send_email() {
    SUBJECT="Git Operations Completed"
    BODY="Git operations (add, commit, push) have been completed successfully."

    echo "$BODY" | mail -s "$SUBJECT" bayizeremarius119@gmail.com
}

# Call the send_email function
send_email

