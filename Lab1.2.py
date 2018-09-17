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

def bruteforce(password_guess,password_MAX, password_size):
    password_guess = '{:d}'.format(password_guess).zfill(password_size)

    if password_guess == str(password_MAX):
        print("finished")

    for i in range(0, len(hash_password)-1, 1):
        password_and_salt = str(password_guess) + salt_value[i]
        if hash_with_sha256(password_and_salt) == hash_password[i]:
            print("user[", i,"]", " Password: ", password_guess)

    bruteforce(int(password_guess) + 1, password_MAX, password_size)


def main():
    '''
    hex_dig = hash_with_sha256('This is how you hash a string with sha256')
    print(hex_dig) #TEST
    print(hash_password[0]) #TEST
    '''
    password_size = int(input("Enter the size of the password(3-7 characters): "))
    password_MAX = int(password_max(password_size))
    password_guess = 0
    sys.setrecursionlimit(10000)
    bruteforce(password_guess, password_MAX, password_size)


main()

