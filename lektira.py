string = input()
def split_rev_comb(s, pos1, pos2):
    return s[:pos1][::-1], s[pos1:pos2][::-1], s[pos2:][::-1]

words = []
for i in range(1, len(string)):
    for j in range(i+1, len(string)):
        words.append(''.join(split_rev_comb(string, i , j)))

words.sort()
print(words[0])

