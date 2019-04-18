with open("test_poly.txt") as fl:
    for poly in fl:
        s = poly
string = []
for char in s:
    string.append(char)
del string[-1]
#print(string)

def reaction(string_list):
    i = 0
    while i < len(string_list):
        a = string_list[i]
        b = string_list[(i+1)]
        if (a.lower() == b.lower() and
                ((a.isupper() and b.islower()) or
                 (a.islower() and b.isupper()))):
            del string_list[i]
            del string_list[i]
            if i <= 0:
                i = 0
            else:
                i -= 1
        else:
            i += 1
        if (i+1) == len(string_list):
            break
    #print("Polymer after reactions: " + ''.join(string_list))
    #print("Polymer consist: " + str(len(string_list)) + " units")
units = set(char.lower() for char in string)
#print(units)


def remove_values_from_list(the_list, val):
    temp_list = ''.join(the_list[:])
    temp_list.replace(val, '')
    temp_list.replace(val.upper(), '')
    er = list(temp_list)
    print(er)


len_list = []
for c in units:
    the_list = string[:]
    print("current unit: " + str(c))
    lista = ''.join(the_list[:])
    print(lista)
    lista.replace(str(c), '')
    lista.replace(str(c).upper(), '')
    b = list(lista)

    reaction(b)
    len_list.append(len(b))

print(len_list)
