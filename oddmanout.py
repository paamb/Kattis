cases = int(input())

for i in range(cases):
    num_guests = int(input())
    guests = [int(x) for x in input().split()]
    if(num_guests == 1):
        print("Case #" + str(i+1) + ":", guests[0])
    guests.sort()
    last = True
    for j in range(0, len(guests)-1, 2):
        if guests[j] != guests[j+1]:
            print("Case #" + str(i+1) + ":", guests[j])
            last = False
            break
    if last:
        print("Case #" + str(i+1) + ":", guests[-1])