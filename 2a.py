from collections import *
import re
twice = 0
triple = 0
with open("ids.txt") as fl:
    for line in fl:
        cnt = Counter()
        letters = re.findall(r'[a-z]', line)
        for l in letters:
            cnt[l] += 1
        #print(cnt)
        if 2 in cnt.values():
            twice += 1
        if 3 in cnt.values():
            triple += 1
print("checksum: " + str(twice*triple))
