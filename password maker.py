import random

alphabet = 'abcdefghijklmnopqrstupwxyz1234567890~!@#$%^&*_+:"<>?|'
tries = 1
while tries > 0:
    answer = str(input('would you like a new 16 letter passport generated for you? Yes/no ')).lower()
    if answer == 'yes': 
        password = ''.join(random.choices(alphabet, k=16))  # k = length of password
        print(password)
    elif answer == 'no':
        print('thank you and goodbye.')
    else:
        print('error')
