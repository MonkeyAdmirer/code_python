firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
birthYear = int(input("Enter your birth year: "))

print(f"Hello {firstName}  {lastName}.")
print(f"You are {2024 - birthYear} years old.")

if birthYear > 2005:
    print("You are not old enough to drink.")
else:
    print("You are old enough to drink.")