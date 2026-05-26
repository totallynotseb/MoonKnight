import random

name = input("What is your name? ")

adjectives = ["Sneaky", "Silent", "Clever", "Brave", "Mysterious", "Fierce"]
animals = ["Otter", "Tiger", "Wolf", "Eagle", "Panther", "Fox"]

codename = random.choice(adjectives) + " " + random.choice(animals)

lucky_number = random.randint(1, 99)

print("Agent " + name + ", your codename is " + codename + "!")
print("Your lucky number is " + str(lucky_number) + ".")