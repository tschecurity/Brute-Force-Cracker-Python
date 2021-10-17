import itertools
import string

def guess_password(real):
    #original code string.ascii_lowercase + string.digits
    #chose string.printable for wider variation of guess values
    chars = string.printable
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            print(guess, attempts)
print(guess_password('tgz'))
