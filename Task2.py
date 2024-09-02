string = input('Enter numbers separated by spaces: ')
numbers = string.split()
print(numbers)
max_number = int(numbers[0])
for item in numbers:
    item = int(item)
    if item > max_number:
        max_number = item
print('Max number is', max_number)