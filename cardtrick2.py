n = int(input())
l = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]

inputs = [int(input()) for i in range (n)]
dic = {}

def pop_append(j, letters):
    total_pops = j
    for _ in range (total_pops):
        letter = letters.pop(0)
        letters.append(letter)
    letter = letters.pop(0)
    dic[letter] = j

for i in inputs:
    letters = l[:i]
    for j in range(1, i+1):
        pop_append(j, letters)
    a = sorted(dic.items(), key=lambda x:x[0])
    values = [str(x[1]) for x in a]
    string = " ".join(values)
    print(string)
    for i in range (1, len(values)+1):
        pop_append(i, values) 
    string = ""
    dic.clear()
    letters.clear()
    a.clear()
    values.clear()