# GitNotified
A cron job that notifies you if you haven't pushed to github that day.

Receive a system notification at 11:50PM every night if you haven't yet pushed to GitHub.

**NOTE:** only works for _MacOS_ users (since notification system relies on AppleScript)

## Requirements
This whole thing relies on multiple moving parts, so make sure you have these first:
* MacOS
* python3
* The following Python packages:
    * BeautifulSoup4 (`pip3 install bs4`)
    * requests (may be installed by default)

## Installation
1. Download project
2. Open your Terminal App and navigate to `GitNotified` directory
3. Run `bash install_gn.sh`
   1. Enter your github username when prompted
   2. You may need to give permission depending on your terminal settings
4. You're good to go

## Uninstall / Other Notes
The timing and automation relies on the `crontab` command, so to uninstall run `crontab -r` from anywhere in your terminal.

GitNotified runs _every_ night at **11:50PM**, but you can always change the timing using the cron job syntax in the `install_gn.sh` source file (just run through the installation process again to make sure it takes effect).
