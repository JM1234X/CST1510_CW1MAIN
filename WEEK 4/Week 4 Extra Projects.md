# Week 4 — Extra Practice Projects (Worked Solutions)

---

## Banker Roulette

**Uses:** lists, `random.choice()`

1. Store a list of names in a variable called `friends`.
2. Pick one at random and print it. There are two equally valid ways to
   do this — `random.choice(friends)` directly, or `random.randint()` to
   generate an index into the list. Try both.

```python
import random

friends = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

# Way 1: random.choice picks directly from the list
print(f"{random.choice(friends)} is paying the bill!")

# Way 2: random.randint generates an index
# (randint is inclusive on both ends, so the max index is len - 1)
index = random.randint(0, len(friends) - 1)
print(f"{friends[index]} is paying the bill!")
```

*Adapted from: 100 Days of Code, Day 4.*

---

## Password Generator

**Uses:** lists, `random.choice()`, string building in a loop

1. Ask the user how many letters, how many symbols, and how many numbers
   they want.
2. Store the allowed letters, symbols, and numbers each in their own
   list.
3. **Easy version:** build the password in order — all letters, then all
   symbols, then all numbers — using `random.choice()` in a loop for
   each part.
4. **Hard version:** build one list containing all the randomly chosen
   characters, then use `random.shuffle()` on it before joining it into
   the final password, so the order is different every time.

```python
import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

# ---------- Easy version: ordered ----------
password = ""
for _ in range(nr_letters):
    password += random.choice(letters)
for _ in range(nr_symbols):
    password += random.choice(symbols)
for _ in range(nr_numbers):
    password += random.choice(numbers)
print(f"Easy password: {password}")

# ---------- Hard version: shuffled ----------
chars = []
for _ in range(nr_letters):
    chars.append(random.choice(letters))
for _ in range(nr_symbols):
    chars.append(random.choice(symbols))
for _ in range(nr_numbers):
    chars.append(random.choice(numbers))

random.shuffle(chars)  # shuffles the list in place (returns None)
print(f"Hard password: {''.join(chars)}")
```

*Adapted from: 100 Days of Code, Day 5.*

---

## Blind Auction

**Uses:** dictionaries, looping over `.items()`

1. Ask each bidder for their name and their bid, storing each pair in a
   dictionary: `{name: bid}`.
2. Ask if there's another bidder. If yes, loop back and ask again.
3. Once everyone has bid, loop over the dictionary and work out who bid
   the highest.
4. Print the winner and their bid — never anyone else's, that's the
   point of a *blind* auction.

```python
bids = {}

while True:
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bids[name] = bid

    another = input("Is there another bidder? (yes/no) ").lower()
    if another != "yes":
        break
    print("\n" * 50)  # push earlier bids off screen so nobody sees them

winner = ""
highest_bid = 0
for name, bid in bids.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = name

print(f"The winner is {winner} with a bid of ${highest_bid:.2f}.")
```

*Adapted from: 100 Days of Code, Day 9.*

---

## Coffee Machine

**Uses:** dictionaries, functions (Week 3), nested dicts

A simulated coffee machine with a fixed menu and finite resources.

1. Store the machine's resources in a dict: `{"water": 300, "milk": 200,
   "coffee": 100}` (amounts in ml/g).
2. Store the menu as a dict of dicts, one entry per drink, each with its
   own `cost` and `ingredients`.
3. Ask what drink the user wants. Write a function that checks the
   machine has enough of every resource that drink needs — if not,
   print what's missing and don't make it.
4. If there's enough, deduct the ingredients from resources, take
   payment (just ask for a number, no need to simulate coins), and print
   confirmation.
5. Let the user check resources (`report`) or turn the machine `off` as
   extra commands before ordering.

```python
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {"water": 300, "milk": 200, "coffee": 100}


def check_resources(ingredients):
    """Return a list of the resources that are too low for this drink."""
    missing = []
    for item, amount in ingredients.items():
        if resources.get(item, 0) < amount:
            missing.append(item)
    return missing


def make_drink(name, ingredients):
    """Deduct the ingredients from the machine's resources."""
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {name}. Enjoy!")


def print_report():
    print(f"Water:  {resources['water']}ml")
    print(f"Milk:   {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")


def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            print("Turning off. Goodbye!")
            break
        if choice == "report":
            print_report()
            continue
        if choice not in MENU:
            print("Sorry, that's not on the menu.")
            continue

        drink = MENU[choice]
        missing = check_resources(drink["ingredients"])
        if missing:
            print(f"Sorry, not enough: {', '.join(missing)}.")
            continue

        print(f"That will be ${drink['cost']:.2f}.")
        payment = float(input("Please enter your payment: $"))
        if payment < drink["cost"]:
            print("Sorry, that's not enough money. Payment refunded.")
            continue

        change = round(payment - drink["cost"], 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        make_drink(choice, drink["ingredients"])


coffee_machine()
```

*Loosely adapted from: 100 Days of Code, Day 15 (the original spec is a
downloadable PDF this document doesn't include — this is a trimmed,
self-contained version covering the same core idea: nested dicts +
functions that check and update them).*

---

Stuck on `.get()` vs `[]` for a key that might not exist? That's
`02 - Dictionaries`, section 4, in this folder.
