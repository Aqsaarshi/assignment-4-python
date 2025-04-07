import random 
print('Welcome to your password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?/[]{}|;:,.' 
number = input('Amount of passwords to generate:') 
number = int(number)
length = input('Input your password length: ') 
length = int(length)

print('\nHere are your passwords: ')

for pwd in range(number): 
    password = ''  # Initialize the password string
    for c in range(length):
        password += random.choice(chars)  # Append a random character to password

    print(password)  # Print the generated password
