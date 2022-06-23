'''
project: random password generator

password: abdXWZ-79_97

'''
import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATIONS = string.punctuation
print(LETTERS)
print(NUMBERS)
print(PUNCTUATIONS)

def password_generator(length = 8):
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATIONS}'
    
    printable = list(printable)
    random.shuffle(printable)

    random_password = random.choice(printable, k=length)
    random_password = ''.join(random_password)
    return random_password


def main():
    password = password_generator()
    print(password)




if __name__ == "__main__":
    main()
