people = int(input())
link = [i for i in range(people)]
size = [1 for i in range(people)]
gifts_gotten = [0 for i in range(people)]
def find(x):
    while(x != link[x]):
        x = link[x]
    return x

def same(a,b):
    return find(a) == find(b)

def unite(a,b):
    a = find(a)
    b = find(b)
    if size[a] < size[b]:
        a,b = b,a
    size[a] += size[b]
    link[b] = a
    
for i in range(people):
    gift_to = int(input())
    gift_to -= 1
    gifts_gotten[gift_to] += 1
    unite(i, gift_to)

cycles = {}
for i in range(people):
    gift = gifts_gotten[i]
    hasKey = False
    for key in cycles.keys():
        if same(key, i):
            if gift == 0:
                cycles[key] += 1
            hasKey = True
            break
    if not hasKey:
        cycles[i] = 0
        if gift == 0:
            cycles[i] += 1
total_changes = 0
if len(cycles) == 1:
    for value in cycles.values():
        total_changes = value
else:
    for value in cycles.values():
        total_changes += 1
        total_changes += max(0, value - 1)

print(total_changes)
