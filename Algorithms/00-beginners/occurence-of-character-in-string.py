sentence = 'IamJustin.Iam30!!!.findmeatemail@gmail.com'
counts = [0] * 128

for char in sentence:
    char_code = ord(char)
    counts[char_code] = counts[char_code] + 1

print(counts) 

#output

'''
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 5, 0, 1, 1, 2, 1, 1, 0, 4, 0, 0, 2, 6, 2, 1, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
''' 
print()
#using dictionary

string = 'peter-picked-a-piece-of-paper'
counts_dict = {}

for c in string:
    if c not in counts_dict:
        counts_dict[c] = 1
    else :
        counts_dict[c] += 1  

print(counts_dict) 

# {'p': 5, 'e': 6, 't': 1, 'r': 2, '-': 5, 'i': 2, 'c': 2, 'k': 1, 'd': 1, 'a': 2, 'o': 1, 'f': 1}