import re
from functools import reduce
import operator

name = "data"
t_stamp = []
with open(name + "4.txt") as fl:
    for line in fl:
        t_stamp.append(line)

t_stamp.sort()
f = open(name + "_sort.txt", "w")
for i in t_stamp:
    f.write(i)
f.close()

guards = {}
sleep_time = {}
w_t = 0
s_t = 0
sleep = []
s_h = []
with open(name + "_sort.txt", "r") as ts:
    for line in ts:
        if "#" in line:
            match_n = re.search(r'#(\d+)', line)
            if match_n:
                g_name = match_n.group(1)
                if g_name not in guards:
                    guards[g_name] = 0
                    sleep_time[g_name] = []
                #print(guards)
        elif "falls asleep" in line:
            match_ts = re.search(r':(\d+)', line)
            if match_ts:
                #print("asleep: " + match_ts.group(1))
                sleep.append(match_ts.group(1))
                s_h.append(int(match_ts.group(1)))

        elif "wakes up" in line:
            match_tw = re.search(r':(\d+)', line)
            if match_tw:
                #print("wake up: " + match_tw.group(1))
                sleep.append(match_tw.group(1))
                s_h.append(int(match_tw.group(1)))
                if len(sleep) == 2:
                    #print(sleep)
                    s_t = int(sleep[1]) - int(sleep[0])
                    sleep_time[g_name].append(list(range(s_h[0], s_h[1])))
                    #print("sleep time: " + str(s_t))
                    guards[g_name] += s_t
                    sleep = []
                    s_h = []
                    #print(g_name)
#print(guards)
#print(sleep_time)
k = max(guards, key=guards.get)
#print(k)

s_m = sleep_time[k]
s = reduce(operator.concat, s_m)
#print(s)

testListDict = {}
for item in s:
  try:
    testListDict[item] += 1
  except:
    testListDict[item] = 1

g = max(testListDict, key=testListDict.get)
print("Case 1 result: " + str(int(k)*int(g)))

for item in sleep_time:
    item = reduce(operator.concat, item)

#print(sleep_time)
for key in sleep_time:
    #print(len(sleep_time[key]))
    if len(sleep_time[key]) != 0:
        sleep_time[key] = reduce(operator.concat, sleep_time[key])
    else:
        continue

#print(sleep_time)
sleep_t = {}
for key in sleep_time:
    testListDict = {}
    for item in sleep_time[key]:
      try:
        testListDict[item] += 1
      except:
        testListDict[item] = 1
    sleep_time[key] = testListDict
    #print(sleep_time)
    if len(sleep_time[key]) != 0:
        g = max(sleep_time[key], key=sleep_time[key].get)
    else:
        continue
    #t = max(sleep_time[key], key=sleep_time[key][g].get)
    sleep_t[key] = {}
    sleep_t[key][g] = sleep_time[key][g]

print(sleep_t)
