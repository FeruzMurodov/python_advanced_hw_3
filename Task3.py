
string = 'Я иду с мечем судия'
string = string.lower().replace(' ', '')
palindrome = None
for i in range(len(string) // 2):
    if string[i] == string[len(string) - i -1]:
        palindrome = True
    else :
        palindrome = False
print('String is palindrome!') if palindrome is True else print('String is not palindrome!')