print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice1 = input('You are at a crossroad. Go "left" or "right"? ').lower()

if choice1 == "left":
    choice2 = input('You reach a lake. "swim" across or "wait" for a boat? ').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at an island with three doors: red, blue, yellow. Which one? ").lower()
        if choice3 == "yellow":
            print("You found the treasure. You win!")
        elif choice3 == "red":
            print("You got burned by fire. Game over.")
        elif choice3 == "blue":
            print("You were eaten by beasts. Game over.")
        else:
            print("That door doesn't exist. Game over.")
    else:
        print("You were attacked by a trout. Game over.")
else:
    print("You fell into a hole. Game over.")
---
account_a = "Cristiano Ronaldo"
followers_a = 650
account_b = "Taylor Swift"
followers_b = 280

print("Higher or Lower: who has more followers (in millions)?")
print(f"A: {account_a}")
print(f"B: {account_b}")

while True:
    guess = input('Type "A" or "B" (or "quit" to stop): ').upper()

    if guess == "QUIT":
        print("Thanks for playing!")
        break

    if guess == "A" or guess == "B":
        if followers_a > followers_b:
            answer = "A"
        else:
            answer = "B"

        if guess == answer:
            print("Correct")
        else:
            print("Wrong")
    else:
        print("Please type A, B, or quit.")

#number guesser
secret_number = 42
guesses = 0
guess = 0

print("I'm thinking of a number between 1 and 100.")

while guess != secret_number:
    guess = int(input("Make a guess: "))
    guesses += 1

    if guess > secret_number:
        print("Too high.")
    elif guess < secret_number:
        print("Too low.")
    else:
        print(f"Correct! You got it in {guesses} guesses.")
