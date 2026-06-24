# Movie Ticket Price Calculator

age = int(input("Enter your age: "))

if age < 13:
    price = 8
elif age >= 65:
    price = 10
else:
    price = 12

print("Ticket price: $", price)