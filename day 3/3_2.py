f = open("input.txt", "r")

lines = [line.strip() for line in f]

f.close()







def iterateOxy(iterable, pos = 0):
    if len(iterable) == 1:
        return iterable[0]
    
    count = 0
    totalCount = 0
    for item in iterable:
        totalCount += 1
        count += int(item[pos])


    if count >= totalCount/2:
        keep = "1"
    else:
        keep = "0"
        
    leftovers = [it for it in iterable if it[pos] == keep ]

    pos += 1
    
    return iterateOxy(leftovers, pos)



def iterateCO(iterable, pos = 0):
    if len(iterable) == 1:
        return iterable[0]
    
    count = 0
    totalCount = 0
    for item in iterable:
        totalCount += 1
        count += int(item[pos])
    
    if count < totalCount/2:
        keep = "1"
    else:
        keep = "0"
        
    leftovers = [it for it in iterable if it[pos] == keep ]

    pos += 1
    
    return iterateCO(leftovers, pos)


def bin_to_dec(binary):
    pointer = 1
    decimal = 0

    for nr in binary[::-1]:

        if nr == "1":
            decimal += pointer
            
        pointer *= 2
        
    return decimal









oxy = iterateOxy(lines)

co = iterateCO(lines)

print(oxy)
print(co)

oxyDec = bin_to_dec(oxy)
coDec = bin_to_dec(co)
print("%d * %d = %d" % (oxyDec, coDec, oxyDec * coDec))





