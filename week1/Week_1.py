#Task 0

print("")
print(">Robins will wear their feathery fire,")
print(">Whistling their whims on a low fence-wire;")
print(">And not one will know of the war,")
print(">not one")
print("")

#Task 1

print("")
print(">House in a week")
print(24*7)
print(">Minutes in a week")
print(60*24*7)
print(">seconds in a week")
print(60*60*24*7)
print("")

#Task 2 

name_i = input(">Whats is your name?")
email_i = input(">what is your email address?")
nickname_i = input(">What is your nickname?")

print("")
print(">##Let's review your information##")
print(">")
print(">Your name: " + name_i)
print(">Your email: " + email_i)
print(">Your nickname: " + nickname_i)
print("")

#Task 3

name_i = input(">Name: ")
victim_i = input(">Victim: ")

print("")
print(">Thank you, " + name_i)
print(">But our " + victim_i + " is in another castle!")
print("")

#Task 4 

name = "Courier"
age = "34"
country = "New Vegas"

print("")
print(f">Hi {name} , you are {age} years old. You live in {country} . ")
print("")

#Task 5 

name = "Ozan Akyol"
age = 18
skill1 = "python"
level1 = "beginner"
skill2 = "2d art"
level2 = "beginner"
lower = 2000
upper = 3000

print("")
print(f">My name is {name}, I am {age} years old ")
print(">")
print(">My skills are")
print(f"> - {skill1} {level1}")
print(f"> - {skill2} {level2}")
print(">")
print(f"My salary expectation is {lower} - {upper} euros/month")
print("")

#Task 6 

number1 = 3
number2 = 5

ans_add = number1 + number2
ans_sub = number1 - number2
ans_mult = number1 * number2
ans_div = number1 / number2

print("")
print(f">number 1 is: {number1}")
print(f">number 2 is: {number2}")
print(">")
print(f">{number1} + {number2} = {ans_add}")
print(f">{number1} - {number2} = {ans_sub}")
print(f">{number1} * {number2} = {ans_mult}")
print(f">{number1} / {number2} = {ans_div}")
print("")

#Task 7 

weight = input(">Enter your weight: ")
height = input(">Enter your height: ")

weight_int = int(weight)
height_int = int(height)

BMI = weight_int / (height_int/100)**2

print(">")
print(f">Your BMI is {BMI} ")

#Task 8

gameName = input(">Game name: ")
gameYear = input(">Which year was this game released? ")

year_int = int(gameYear)

ans = 2025 - year_int

print(">")
print(f">{gameName} is {ans} years old.")
print("")

#Task 9

number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
product = number1 * number2 * number3
print("The product is", product)

#Task 10

cafeteria_i = input(">How many times a week do you eat at the student cafeteria? ")
lunch_i = input(">The price of a typical student lunch? ")
groceries_i = input(">How much money do you spend on groceries in a week? ")

cafeteria_int = int(cafeteria_i)
lunch_int = int(lunch_i)
groceries_int = int(groceries_i)

ansDaily = ((cafeteria_int*lunch_int) + groceries_int)/7
ansWeek =  (cafeteria_int*lunch_int) + groceries_int
ansMonth = ((cafeteria_int*lunch_int) + groceries_int)/7*30

print(">")
print(">Average food expenditure:")
print(f">Daily: {ansDaily}")
print(f">Weekly: {ansWeek}")
print(f">Montly: {ansMonth}")
print("")


