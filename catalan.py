numbers = [1]
fak2 = 1
fak = 1
for i in range(1,5001):
    fak2 *= (2*i)*(2*i-1)
    fak *= i
    numbers.append(fak2//(fak*(fak*(i+1))))

num_inputs = int(input())
for i in range(num_inputs):
    catalan_number = int(input())
    print(numbers[catalan_number])