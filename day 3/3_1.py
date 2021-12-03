f = open("input.txt", "r")

cols = [[] for _ in range(12)]

for line in f:
    for i in range(len(line.strip())):
        cols[i].append(int(line[i]))

f.close()

gamma = ""
epsilon = ""

for col in cols:
    if len(col)/2 < sum(col):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"


print(gamma)
print(epsilon)


def bin_to_dec(binary):
    pointer = 1
    decimal = 0

    for nr in binary[::-1]:
        if nr == "1":
            decimal += pointer
        pointer *= 2
    return decimal

gammaDec = bin_to_dec(gamma)
epsilonDec = bin_to_dec(epsilon)

print(gammaDec * epsilonDec)



