string1 = input('Enter the first word: ')
string2 = input('Enter the second word: ')
chars_array1 = []
chars_array2 = []

for char in string1:
    chars_array1.append(char)
for char in string2:
    chars_array2.append(char)

#print(chars_array1, type(chars_array1))
#print(chars_array2, type(chars_array2))

if len(chars_array1) == len(chars_array2):
    for char1 in chars_array1:
        for char2 in chars_array2:
            if char1 == char2:
                chars_array2.remove(char2)
    if len(chars_array2) == 0:
        print('Words are anagrams!')
        exit()
    else:
        print('Words are not anagrams!')
else:
    print('Words are not anagrams!')