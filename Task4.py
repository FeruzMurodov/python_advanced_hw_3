import random
import string

size = int(input('Enter the size of the pasword: '))
password = ''
for i in range(size):
     temp_char = random.choice(string.ascii_letters + string.digits + string.punctuation)
     password = password + temp_char
print(password)