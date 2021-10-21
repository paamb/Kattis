num_val = int(input())
values = [int(x) for x in input().split()]

values.sort(reverse = True)
disscount = 0
for i in range(2, num_val, 3):
    disscount += values[i]
print(disscount)