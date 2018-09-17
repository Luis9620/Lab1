import sys
import hashlib

salt_file = open("salts")
hash_file = open("hashPasswords")
salt_value = salt_file.read().split(',')
hash_password = hash_file.read().split(',')


def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


'''
def formatting_password(password_size): #formatting_paswords using if statements
    if password_size == 3:
        return '{:d}'.format(0).zfill(3)
    elif password_size == 4:
        return '{:d}'.format(0).zfill(4)
    elif password_size == 5:
        return '{:d}'.format(0).zfill(5)
    elif password_size == 6:
        return '{:d}'.format(0).zfill(6)
    elif password_size == 7:
        return '{:d}'.format(0).zfill(7)
    else :
        print("Invalid input.")

def formatting_password2(password_size): #formatting_paswords using dictionary
    return {
        3: '{:d}'.format(0).zfill(3),
        4: '{:d}'.format(0).zfill(4),
        5: '{:d}'.format(0).zfill(5),
        6: '{:d}'.format(0).zfill(6),
        7: '{:d}'.format(0).zfill(7)
    }.get(password_size, "Invalid input")
'''


def password_max(password_size):
    if password_size == 3:
        return 999
    elif password_size == 4:
        return 9999
    elif password_size == 5:
        return 99999
    elif password_size == 6:
        return 999999
    elif password_size == 7:
        return 9999999


def bruteforce(password_guess, password_MAX, password_size):
    for i in range(0, len(hash_password) - 1, 1):
        for j in range(0, password_MAX, 1):
            password_guess = '{:d}'.format(j).zfill(password_size)
            password_and_salt = str(password_guess) + salt_value[i]
            if hash_with_sha256(password_and_salt) == hash_password[i]:
                print("user[", i,"]", " Password: ", password_guess)
    bruteforce(int(password_guess), password_MAX, password_size)


def main():
    password_size = int(input("Enter the size of the password(3-7 characters): "))
    password_MAX = int(password_max(password_size))
    sys.setrecursionlimit(100000)
    number_of_users = len(hash_password)
    bruteforce(0, password_MAX, password_size)


main()
