import io, os
input = io.BytesIO(os.read(0, \
    os.fstat(0).st_size)).readline
nums, queries = [int(x) for x in input().decode().split(" ")]
link = [int(i) for i in range(nums)]
size = [1 for i in range(nums)]

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

for i in range(queries):
    operat, val1, val2 = input().decode().split(" ")
    val1, val2 = int(val1), int(val2)
    if(operat == '='):
        unite(val1,val2)
    elif(operat == '?'):
        if(same(val1,val2)):
            print("yes")
        else:
            print("no")
