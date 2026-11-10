
print("Welcome to the Band Name Generator!")

city = input("What city did you grow up in?\n")
pet = input("What is the name of a pet?\n")

band_name = f"{city} {pet}"
print(f"Your band name could be: {band_name}")



print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
people = int(input("How many people are splitting the bill? "))
tip = int(input("What percentage tip would you like to give? e.g. 12 for 12%: "))

each_person = (bill / people) * (1 + tip / 100)

print(f"Each person should pay: ${each_person:.2f}")


