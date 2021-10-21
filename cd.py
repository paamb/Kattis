while True:    
    N,M = [int(x) for x in input().split()]
    
    if M == N == 0:
        break
    cds = []
    counter = 0
    for i in range(N):
        a = int(input())
        cds[a] = True

    for j in range(M):
        b = int(input())
        try:
            if cds[b] == True:
                counter += 1
        except KeyError:
            continue
    
    print(counter)