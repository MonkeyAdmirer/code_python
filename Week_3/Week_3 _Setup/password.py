import random

print("Welcome to our password generating app!")

pwd_length = int(input("Enter the length of the password: "))

lowercase = list(range(97, 123))
uppercase = list(range(65, 91))
digits = list(range(48, 58))
special = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))

pwd_symbols = lowercase.copy()

has_upper = input("Include upper case characters? (y/n): ")
if has_upper in 'yY':
    pwd_symbols.extend(uppercase)

has_special = input("Include special characters? (y/n): ")
if has_special in 'yY':
    pwd_symbols.extend(special)

has_digits = input("Include digits? (y/n): ")
if has_digits in 'yY':
    pwd_symbols.extend(digits)

new_password = "" # Empty string to hold our new password

while len(new_password) != pwd_length:
    random_symbol = chr(random.choice(pwd_symbols))
    new_password = new_password + random_symbol
# end of while loop

print(f"{new_password} has been generated.")