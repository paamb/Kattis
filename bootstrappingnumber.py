import math
def binarySearch(n):
    top = 10
    bottom = 0
    val = 5
    error = math.inf
    while error > 10**-6:
        if (math.log(n) > val*math.log(val)):
            bottom = val
        else:
            top = val
        val = (top+bottom)/2
        error = abs(math.log(n)-val*math.log(val))
    return val
print(binarySearch(int(input())))