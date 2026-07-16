# Password Strength Checker

password = input("Enter Password: ")

upper = False
lower = False
digit = False
special = False

# Check each character
for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

# Check password strength
if len(password) >= 8 and upper and lower and digit and special:
    print("Strong Password")
else:
    print("Weak Password")
    print("Missing Conditions:")

    if len(password) < 8:
        print("• Minimum 8 characters")

    if not upper:
        print("• At least one uppercase letter")

    if not lower:
        print("• At least one lowercase letter")

    if not digit:
        print("• At least one digit")

    if not special:
        print("• At least one special character")