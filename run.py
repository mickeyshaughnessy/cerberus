import os, time

RATE, WORKERS, DUR = 1000, 40, 30
while True:

    with open('targets.txt') as f:
        for line in f:
            url = line.rstrip()
            os.run("""
                    echo "GET %s" |
                    vegeta attack -rate=%s -workers=%s -duration=%ss | 
                    tee results.bin | 
                    vegeta report""" % (url, RATE, WORKERS, DUR))
            os.run('cat results.bin | vegeta plot > plot.html')
            print("Finished testing %s, napping" % url)
            time.sleep(5)
