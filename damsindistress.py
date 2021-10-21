n, w = [int(x) for x in input().split()]
relation_matrix = [[] for _ in range(n)]
matrix = []
d_finish, c_finish, u_finish = [int(x) for x in input().split()]
weigths = [0 for _ in range(n)]
weigths[0] = c_finish-u_finish
matrix.append((c_finish,u_finish))
for i in range(1,n):
    d, c, u = [int(x) for x in input().split()]
    relation_matrix[d-1].append(i) 
    matrix.append((c,u))

# print(relation_matrix)
for i in range(len(relation_matrix)):
    for index in relation_matrix[i]:
        c = matrix[index][0]
        u = matrix[index][1]
        weigths[index] = c - u + max(0, weigths[i] - c) + max(0, w )
weigths.append(w)
print(min(weigths))