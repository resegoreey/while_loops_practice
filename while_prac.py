#countdown timer
print("Count down to zero")
user_num = int(input("Enter a number greater than zero: "))

while user_num > 0:
    user_num -= 1
    print(user_num)
print()

# sum of numbers 
sum = 0
number = int(input("Enter a number(0 to stop): "))

while number != 0:
    sum += number

    number = int(input("Enter another number( 0 to stop): "))
    if number == 0:
        print(f"Total: {sum}")
        print("bye!")
        break
    #print(sum)
print()

# Guess the number
guesses = 0
random_num = 20
guess = int(input("Guess a number between 1 and 21: "))
while guess != random_num:
    if guess < random_num:
        print("You went bit lower, try again")
    elif guess > random_num:
        print("You went a higher. Try going down")

    guesses += 1
    print(f"Number of guess: {guesses}")
    guess = int(input("Guess again: "))
print(f"You guessed it right after {guesses} guesses")
print()

#Even Number Checker
