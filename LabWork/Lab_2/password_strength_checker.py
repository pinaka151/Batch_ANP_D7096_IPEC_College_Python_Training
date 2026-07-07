'''----------------------Password Strength Checker----------------------'''

# Function to check password strength
def check_password(password):

    upper = 0
    lower = 0
    digit = 0

    if(len(password) < 8):
        return "Weak Password"

    for i in password:

        if(i.isupper()):
            upper += 1

        elif(i.islower()):
            lower += 1

        elif(i.isdigit()):
            digit += 1

    if(upper >= 1 and lower >= 1 and digit >= 1):
        return "Strong Password"

    else:
        return "Weak Password"


# Main Program
password = input("Enter Password: ")

result = check_password(password)

print(result)