for i in range(int(input())):
    coke, one, five, ten = [int(x) for x in input().split()]
    coins = 0
    for i in range(coke):
        if(ten > 0):
            if five + ten < coke - i and one > 2:
                ten -= 1
                one += 3
                five += 1
                coins += 4
            else:
                ten -= 1
                one += 2
                coins += 1
        elif five / 2 >= coke-i and five > 1:
            five -= 2
            one += 2
            coins += 2
        elif five > 0 and one > 2:
            five -= 1
            one -= 3
            coins += 4
        elif one > 7:
            one -= 8
            coins += 8
    print(coins)

