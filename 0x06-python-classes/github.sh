#!/usr/bin/bash

token="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"

git add . | git commit -m "0x06. Python - Classes and Objects" | git push

#echo "System, please enter your username on GitHub (must be $token):"
entered_username = $token

if [ "$entered_username" == "$token" ]; then
    echo "Successfully, the username is set to: $token"
    echo "Next step: Enter your password" 
    entered_password = $token
    if [ "$entered_password" == "$token" ]; then
        echo "Successfully, the password is accepted $token"
        echo "Next step: Check GitHub"
    else
        echo "Failed: Incorrect password"
    fi
else
    echo "Failed: Incorrect username"
fi

