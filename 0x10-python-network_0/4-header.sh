#!/bin/bash

# Check if the number of arguments is not equal to 1
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Set the URL from the command-line argument
url="$1"

# Use curl to send a GET request with the specified header
curl -sH "X-School-User-Id: 98" "$url"

