num_days = int(input())

prev = 1000000000
money = 100
for i in range(num_days):
    curr = int(input())
    if prev < curr:
        money += min((money // prev), 100000) * (curr-prev)
    prev = curr
print(money)