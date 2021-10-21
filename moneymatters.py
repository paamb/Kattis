import time
start_time = time.time()
input1 = input().split(" ")
friends = int(input1[0])
friendships = int(input1[1])
sums = []
salaryList = []
for i in range (friends):
    salaryList.append(int(input()))

finalSums = []
friendGroups = []
for i in range(friendships):
    friends = input().split()
    f1 = int(friends[0])
    f2 = int(friends[1])
    if(friendGroups == []):
        friendGroups.append([f1,f2])
        finalSums.append(salaryList[f1]+salaryList[f2])
        continue

    added = False
    for i in range(len(friendGroups)):
        if(f1 in friendGroups[i]):
            friendGroups[i].append(f2)
            finalSums[i]+=salaryList[f2]
            added = True
        elif (f2 in friendGroups[i]):
            friendGroups[i].append(f1)
            finalSums[i]+= salaryList[f1]
            added = True

    if(not added):
        friendGroups.append([f1,f2])
        finalSums.append(salaryList[f1]+salaryList[f2])
impossible = False
for element in finalSums:
    if (element != 0):
        print("IMPOSSIBLE")
        impossible = True
        break

if(not impossible):
    print("POSSIBLE")

print(time.time()-start_time)