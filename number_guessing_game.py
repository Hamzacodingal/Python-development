print("Guess the number (Hint: It's one of these: 10, 20, 30, 40, 50)")

while True:
    guess = int(input("Your guess: "))
    if guess == 10:
        print("Correct! The number is 10.")
        break
    if guess == 20:
        print("Correct! The number is 20.")
        break
    if guess == 30:
        print("Correct! The number is 30.")
        break
    if guess == 40:
        print("Correct! The number is 40.")
        break
    if guess == 50:
        print("Correct! The number is 50.")
        break
    print("Incorrect! Try again.")

