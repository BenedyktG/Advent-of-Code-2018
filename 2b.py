from collections import *
from difflib import SequenceMatcher
temp = []
ratio = 0
ratios = []
def similar(a, b):
    ratio = (SequenceMatcher(None, a, b).ratio())
    ratio = round(float(ratio)*100,1)
    return ratio

with open("ids.txt") as fl:
    for line in fl:
        temp.append(line)
pr = round(((len(temp[0])-1)/(len(temp[0])))*100, 0)
print(pr)
i = 0
while i < len(temp):
    a = temp[i]
    #print("first string: " + a)
    for x in temp[1:]:
        b = x
        if similar(a, b) > pr and similar(a, b) < 100:
            la = list(a)
            print(a)
            lb = list(b)
            print(b)
            for i in range(len(la)-1):
                if la[i] != lb[i]:
                    la.remove(la[i])
                    lb.remove(lb[i])
                    
            print(''.join(la))


            temp.remove(a)
            temp.remove(b)
    i += 1
