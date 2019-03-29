#!/usr/bin/env bash

asPath=`which osascript`
pyPath=`which python3`
mpyPath="$PWD/src/main.py"
njsPath="$PWD/src/notify.js"

read -p "Enter Github Username: " -a githubName
job="50 23 * * * $pyPath $mpyPath $asPath $njsPath $githubName"

echo "$job" > ctab.txt
crontab ctab.txt
rm ctab.txt

echo "[ Installed ]"
