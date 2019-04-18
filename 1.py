freq = 0
freqs = [0]
ans = []
with open("1.txt") as fl:
    for line in fl:
        freq += int(line)
        freqs.append(freq)
for i in range(1, len(freqs)):
    rng = i-1
    #print(freqs[i])
    if freqs[i] in freqs[:rng]:
        ans.append(freqs[i])
#print(freqs)
while len(ans) == 0:
    with open("1.txt") as fl:
        for line in fl:
            freq += int(line)
            freqs.append(freq)
            if freq in freqs[:-2]:
                ans.append(freq)
                print("First twice freq: " + str(ans))
                break


#print(freq)
#print(freqs)
