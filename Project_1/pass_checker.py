import string

password = input("Enter your password: ")

has_digit = False
has_uppercase = False
has_symbol = False

# Check each character in the password
for char in password:
    if char.isdigit():
        has_digit = True

    if char.isupper():
        has_uppercase = True

    if char in string.punctuation:
        has_symbol = True


# Determine password strength
if len(password) >= 12 and has_digit and has_uppercase and has_symbol:
    print("Strong password.")

elif len(password) >= 8 and has_uppercase and has_symbol:
    print("Medium password.")

else:
    print("Weak password.")