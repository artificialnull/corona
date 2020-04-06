import json
f = open('covid.txt').read().split('\n')
cases = {}
for line in f:
    if len(line) == 0:
        continue
    ls = line.split(',')
    cases[ls[3]] = int(ls[4])
print('[')
for line in open('counties.txt').read().split('\n'):
    ls = line.split('\t')
    if not len(ls) > 1:
        continue
    ident = ls[0]
    lat = float(ls[-2][:-1])
    lon = -float(ls[-1][1:-1])
    c = cases.get(ls[2], 0)
    for x in range(0, c):
        print(json.dumps({
            'id': str(ident) + '-' + str(x),
            'latitude': lat,
            'longitude': lon,
            }) + ',')
print(']')
