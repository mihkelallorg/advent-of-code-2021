d = 0
h = 0
a = 0

f = open("advent2.txt", "r")

for line in f:
    items = line.split()
    if len(items) != 2:
        break
    cmd = items[0]
    l = int(items[1])

    if cmd == "forward":
        h+=l
        d+=a*l
    elif cmd == "down":
        a+=l
    elif cmd == "up":
        a-=l

f.close();

print(d*h)

