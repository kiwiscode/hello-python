print("Hello World")

# User Input
name = input("What is your name? ")
print("Hello " + name)

age = input("How old are you? ")
print("Okay, so you are " + age + " years old.")

# Addition of two numbers
firstNum = input("First number: ")
secondNum = input("Second number: ")
total_sum = float(firstNum) + float(secondNum)
print("The sum is: " + str(total_sum))

# String operations
string = "Python for beginners"
print(string)

# Find and replace
print("Index of 'n':", string.find("n"))
print("Replaced string:", string.replace("beginners", "intermediate level developers"))

# Price comparisons
price = 25
print("Is the price greater than 20 or less than 30?", price > 20 or price < 30)
print("Is the price greater than 20 and greater than 25?", price > 20 and price > 25)
print("Is the price not less than 25?", not price < 25)
print("Is the price not greater than 20?", not price > 20)

# Temperature check
temperature = 28

if temperature > 30:
    print("The weather is nice; no need to take a jacket.")
elif 25 < temperature <= 30:
    print("The weather is warm, but you might want to bring a light jacket just in case.")
else:
    print("It's a bit cold outside; better to take your jacket with you.")

numbers = [0,1,2,3,4,5,6]
print("Numbers Before insert: ",numbers)

person = {
    "name": "John",
    "age": "28",
    "surname": "Doe"
}

numbers.insert(3,person)
print("Numbers After insert: ",numbers)


numbers.pop(3)

sum = 0
print("Sum before loop:",sum)
for item in numbers:
    sum += item
print("Sum after loop:",sum)




