freq = 0
freqs = [0]
ans = []
while len(ans) == 0:
    with open("1.txt") as fl:
        for line in fl:
            freq += int(line)
            freqs.append(freq)
            print(freq)
            if freq in freqs[:-2]:
                ans.append(freq)
                print("First twice freq: " + str(ans))
                break



#print(freq)
#print(freqs)
