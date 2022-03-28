import random

print("Welcome to my password generator")
print("------------------------------------")

char1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*()_-'
char2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'



length_password = input("type the password length: ")
length_password = int(length_password)
caracters = input("use special caracters(y/n): ")
password = ''



if caracters == 'y':
    for c in range(length_password):
        password += random.choice(char1)
    print("\nPassword: ", password)
elif caracters == 'n':
    for c in range(length_password):
        password += random.choice(char2)
    print("\nPassword: ", password)
else:
    print("\nCaracter inválido")

