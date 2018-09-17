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

def bruteforce(password_guess, password_MAX, password_size,number_of_users):
    if number_of_users == len(hash_password):
        print("finished")
    for i in range(0, password_MAX, 1):
        password_guess = '{:d}'.format(i).zfill(password_size)
        password_and_salt = str(password_guess) + salt_value[number_of_users]
        if hash_with_sha256(password_and_salt) == hash_password[number_of_users]:
            print("user[", number_of_users, "]", " Password: ", password_guess)

    bruteforce(int(password_guess), password_MAX, password_size, number_of_users+1)


def main():
    '''
    hex_dig = hash_with_sha256('This is how you hash a string with sha256')
    print(hex_dig) #TEST
    print(hash_password[0]) #TEST
    '''
    password_size = int(input("Enter the size of the password(3-7 characters): "))
    password_MAX = int(password_max(password_size))
    password_guess = 0
    number_of_users = 0
    sys.setrecursionlimit(10000)
    bruteforce(password_guess, password_MAX, password_size,number_of_users)


main()

