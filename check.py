import requests
import os, time

bench = ["www.google.com", "www.nytimes.com", "www.amazon.com", "www.president.gov.ua", "www.usa.gov"]
bench = ["https://" + b for b in bench]

while True:
    targets = []
    os.system('clear')
    print("References:")
    for b in bench:
        try:
            r = requests.get(b, timeout=1)
        except:
            r = "failed"
        print(b + " : " + str(r))
    print("===================")
    with open("all_urls.txt") as f:
        for line in f:
            line = line.rstrip()
            try:
                r = requests.get(line, timeout=1)
                targets.append(line)
            except:
                r = "failed"
            print(line.rstrip() + " : " + str(r))
    with open("targets.txt", "w") as f:
        for t in targets:
            f.write(t+'\n')
    print("finished checking domains, napping")
    time.sleep(5)
