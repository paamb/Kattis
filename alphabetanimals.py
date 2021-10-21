prev = input()
 
num_ani = int(input())
animals = []
right_start_letter = []
for i in range(num_ani):
    animal = input()
    animals.append(animal)
    if animal[0] == prev[-1]:
        right_start_letter.append(animal)

def find_ani():
    for i in range(len(right_start_letter)):
        for j in range(num_ani):
            if right_start_letter[i][-1] == animals[j][0] and right_start_letter[i] != animals[j]:
                break
            if j == num_ani-1:
                print(right_start_letter[i] + '!')
                return
    print(right_start_letter[0])

if len(right_start_letter) > 0:
    find_ani()
else:
    print('?')
    