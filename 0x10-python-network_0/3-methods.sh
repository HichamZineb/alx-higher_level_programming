#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
[ $# -eq 1 ] && curl -sI -X OPTIONS "$1" | grep -i "allow" | cut -d ' ' -f2-
