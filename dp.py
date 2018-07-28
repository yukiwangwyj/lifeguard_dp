# input data
with open('/Users/yukiwang/Desktop/cmu/data/10.in', 'r') as f:
    size = int(f.readline())
    arrList = []
    for line in f:
        arrList.append(list(map(int, line[:-1].split(" "))))
pair = sorted(arrList, key=lambda x: (x[0], -x[1]))
maxEnd = pair[0][1]
overLap = False
f = []  # exclude current one
g = []  # include current one, previous excluded
h = []  # include current one, Not previous excluded
notOverlap = []

for n in range(0, size):
    if len(notOverlap) == 0:  # n = 1
        f.append(0)
        h.append((pair[0][1]-pair[0][0]))
        g.append(None)
        notOverlap.append(pair[0])
    elif len(notOverlap) == 1:   # n = 2
        f.append(h[0])
        h.append(h[0]+pair[1][1]-(max(pair[1][0], pair[0][1])))
        g.append(pair[1][1]-pair[1][0])
        notOverlap.append(pair[1])
    else:
        if pair[n][1] > maxEnd:
            maxEnd = pair[n][1]
            f.append(h[-1])
            h.append(h[-1]+pair[n][1]-max(pair[n][0], notOverlap[-1][1]))
            g.append(max(
                (g[-1] + pair[n][1] - max(pair[n][0], notOverlap[-1][1])),
                (f[-2] + pair[n][1] - max(pair[n][0], notOverlap[-2][1])))
            )
            notOverlap.append(pair[n])
        else:
            overLap = True

if overLap == True:
    output = h[-1]
else:
    output = max(f[-1], g[-1])

print(output)

final = open('/Users/yukiwang/Desktop/cmu/data/10.out', 'w')
final.write(str(output))




