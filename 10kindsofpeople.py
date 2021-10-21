r, c = [int(x) for x in input().split(" ")]
matrix = [list(input()) for _ in range(r)]
flatten_matrix = [j for sub in matrix for j in sub]
queries = int(input())
pos = [[int(x) - 1 for x in input().split(" ")] for i in range(queries)]
link = [int(i) for i in range(r*c)]
size = [1 for i in range(r*c)]


def find(x):
    x_start = x
    while x != link[x]:
        x = link[x]
    link[x_start]=x
    return x



def makeStructure():
    for i in range(r):
        for j in range(c):
            curr = matrix[i][j]
            if (i+1 != r and matrix[i+1][j]==curr):
                unite(flatten(i,j), flatten(i+1, j))
            if (j+1 != c and matrix[i][j+1]==curr):
                unite(flatten(i,j), flatten(i, j+1))

    
def flatten(a,b):
    return a * c + b

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

def unionfind():
    makeStructure()
    for startX, startY, endX, endY in  pos:
        if(same(flatten(startX, startY), flatten(endX,endY))):
            if(matrix[startX][startY] == '1'):
                print("decimal")
            else:
                print("binary")
        else:
            print("neither")
    return None


unionfind()

