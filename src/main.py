import sys
import subprocess
from bs4 import BeautifulSoup
import requests

osascript = sys.argv[1]
notifyjs = sys.argv[2]
link = "https://github.com/" + sys.argv[3]
res = requests.get(link, timeout = 10)

html = BeautifulSoup(res.content, "html.parser")
today = html.find_all("rect")[-1:][0]
contributions = int(today["data-count"])

if contributions == 0:
	subprocess.Popen([osascript, notifyjs])
