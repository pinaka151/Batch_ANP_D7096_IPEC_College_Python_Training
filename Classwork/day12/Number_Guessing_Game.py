# Number Guessing Game

secret_number = 57
attempts = 0

while attempts < 7:
    guess = int(input("Enter your guess: "))

    # Ignore negative numbers
    if guess < 0:
        print("Negative numbers are not allowed. Try again.")
        continue

    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess < secret_number:
        print("Too Low!")

    else:
        print("Too High!")

else:
    print("Sorry! You have used all 7 attempts.")

print("Attempts used:", attempts)