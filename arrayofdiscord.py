num_values = int(input())
values = [int(x) for x in input().split()]
indexed_values = [(values[i], i) for i in range(len(values))]
def main():
    for i in range(len(values)):
        for j in range(10):
            copy_values = list(indexed_values)
            value, index = copy_values.pop(i)
            if j == 0 and value > 9:
                continue

            value_to_string = str(j) + str(value)[1::]
            copy_values.append((int(value_to_string), index))
            copy_values.sort()  
            for k in range(len(values)):
                if indexed_values[k][1] != copy_values[k][1]:
                    return copy_values
    return 0

tupel_list = main()

if tupel_list != 0:
    tupel_list.sort(key = lambda x:x[1])
    valueList = [str(tupel_list[i][0]) for i in range(len(tupel_list))]
    print(' '.join(valueList))
else:
    print("impossible")
