import random

names = []

while True:
    name = input('Enter a name. Leave blank to finish: ')
    if name == '':
        break
    names.append(name)
choice = random.choice(names)
print(f'Congradulations or condolences {choice}!!! your name has been picked out of the hat!')