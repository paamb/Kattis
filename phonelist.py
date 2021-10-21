import math
testcases = int(input())

def check_test_case():
    num_numbers = int(input())
    numbers = []
    for j in range(num_numbers):
        number = input()
        numbers.append(number)
    numbers.sort()

    for i in range(len(numbers)-1):
        num_1 = numbers[i]
        num_2 = numbers[i+1]
        length_num_1 = len(num_1)

        if num_1 == num_2[:length_num_1]:
            return "NO"
    return "YES"

for i in range(testcases):
    print(check_test_case())



