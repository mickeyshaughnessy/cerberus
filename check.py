import requests
import os, time

targets = []
while True:
    with open("urls.txt") as f:
        os.system('clear')
        for line in f:
            try:
                r = requests.get(line.rstrip(), timeout=1)
            except:
                r = "failed"
            print(line.rstrip() + " : " + str(r))
        time.sleep(3)
