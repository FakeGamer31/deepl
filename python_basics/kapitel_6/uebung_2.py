import random

number = random.randint(0,100)
loop = True

while loop:
    print('Bitte geben Sie eine Zahl zwischen 0 und 100 ein.')
    guess = int(input('Zahl: '))
    if guess == number:
        loop = False
    elif guess < number:
        print('Zu klein!')
    elif guess > number:
        print('Zu groß')
print('HGW Zahl gefunden.')