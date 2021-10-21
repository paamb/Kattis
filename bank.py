N, T = [int(x) for x in input().split()]
people = [[] for x in range(N)]
for i in range(N):
    money, time_limit = [int(x) for x in input().split()]
    people[time_limit].append(money)

for j in range(len(people)):
    if(people[j] == []):
        continue
    people[j].sort(reverse=True)

value = 0

for k in range(T):
    if(people[k] == []):
        continue
    value_beeing_added = people[k][0]
    for l in range(k+1, len(people)):
        if(len(people[l]) > l):
            if value_beeing_added < people[l][l]:
                value_beeing_added = people[l][l]

    value += value_beeing_added
print(value)