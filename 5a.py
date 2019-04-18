import sys
with open("polymer.txt") as fl:
    for poly in fl:
        line = poly
#line = [line for line in sys.stdin][0].strip()


def are_opp(a, b):
    return (a.lower() == b.lower() and
            ((a.isupper() and b.islower()) or
             (a.islower() and b.isupper())))


def react(line):
    buf = []
    for c in line:
        #print(c)
        if buf and are_opp(c, buf[-1]):
            buf.pop()
        else:
            buf.append(c)
            #print(buf)
    buf.pop()
    return len(buf)


agents = set([c.lower() for c in line])

# part 1
print(react(line))
