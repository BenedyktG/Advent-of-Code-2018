import numpy as np
import re

count = 0
s = (1000,1000)
mat = np.zeros(s)
with open("input.txt") as fl:
    for line in fl:
        obj = re.findall(r'-?\d+\.?\d*', line)
        #print(obj)
        x = int(obj[1])
        y = int(obj[2])
        spanx = int(obj[3])
        spany = int(obj[4])
        mat[x:x+spanx, y:y+spany] += 1
        #if np.array_equal(np.ones((spanx,spany)), mat[x:x+spanx, y:y+spany]):
            #print("Right ID: " + str(obj[0]))
for x in np.nditer(mat):
    if x > 1:
        count += 1
with open("input.txt") as fl:
    for line in fl:
        obj = re.findall(r'-?\d+\.?\d*', line)
        #print(obj)
        x = int(obj[1])
        y = int(obj[2])
        spanx = int(obj[3])
        spany = int(obj[4])
        #mat[x:x+spanx, y:y+spany] += 1
        if np.array_equal(np.ones((spanx,spany)), mat[x:x+spanx, y:y+spany]):
            print("Right ID: " + str(obj[0]))
print(count)
