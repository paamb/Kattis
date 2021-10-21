houses, cabels = [int(x) for x in input().split()]
link = [int(i) for i in range(houses)]
size = [1 for i in range(houses)]

def find(x):
    x_start = x
    while x != link[x]:
        x = link[x]
    link[x_start]=x
    return x

def unite(a, b):
    a = find(a)
    b = find(b)
    if (same(a, b)):
        return None
    if(size[a] < size[b]):
        a,b = b,a
    size[a] += size[b]
    link[b] = a

def same(a, b):
    return find(a) == find(b)

for i in range(cabels):
    a,b = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    if (a > b):
        a,b = b,a
    unite(a,b)

not_connected_houses = []
for i in range(houses):
    if find(i) != find(0):
        not_connected_houses.append(i)

if len(not_connected_houses) == 0:
    print("Connected")
else:
    for i in range(len(not_connected_houses)):
        print(not_connected_houses[i] + 1)