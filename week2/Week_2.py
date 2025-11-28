#Task 11

Fah_int =  int(input(">Please type in a temperature (F): "))
cal = ((Fah_int) - 32) * 5/9

print(f"{Fah_int} degrees Fahrenheit equals {cal} degrees Celsius")

if cal < 0 :
    print("Brr! It's cold in here!")

#Task 12

hourlyWage_i = float(input("Hourly wage: "))
hoursworke_i = int(input("Hours worked: "))
day = input("Day of the week: ")

cal = hoursworke_i*hourlyWage_i

if day == "Sunday":
    cal = 2*cal

print("")
print(f">Hourly wage: {hourlyWage_i} liras")
print(f">Hours worked: {hoursworke_i}")
print(f">Day of the week: {day}")
print(f">Daily wages: {cal} liras")
print("")

#Task 13

age = int(input(">How old are you? "))

if age < 18:
    print(">You can’t play Dark Souls")

elif age >= 18 and age < 44:
    print(">Here is Dark Souls. Lol")

else:
    print("“You are too old for this sh*t”")

#Task 14

number1 = int(input(">Type the first number: "))
number2 = int(input(">Type the second one: "))

if(number1 > number2):
    print("First one is greater")

elif number1 == number2:
    print("these are equal")

else:
    print("second one is greater")

#Task 15

gName1 = input(">Type the first game name: ")
gName2 = input(">Type the first game name: ")

if gName1 > gName2:
    print(f">{gName1} comes alphabetically last")

elif gName1 == gName2:
    print(">These are same!")

else:
    print(f">{gName2} comes alphabetically last")

#Task 16

clanName = str(input(">Which community do you belong to?: "))

if clanName == "New California Republic" or clanName == "NCR" or clanName ==  "Brotherhood of Steel" or clanName == "Caesar’s Legion" or clanName == "Great Khans" or clanName == "Vault Dweller":
    print(">You’re belong to Fallout Universe.")

else:
    print(">Nope, you are not belong to Fallout Lore")

#Task 17

grade = int(input(">How many points [0-100]: "))

if grade < 0:
    print(">Grade: YOU WHAT?")

if grade > -1 and grade <50:
    print(">Grade: fali?")

if grade > 49 and grade <60:
    print(">Grade: 1")

if grade > 59 and grade <70:
    print(">Grade: 2")

if grade > 69 and grade <80:
    print(">Grade: 3")

if grade > 79 and grade <90:
    print(">Grade: 4")

if grade > 89 and grade <101:
    print(">Grade: 5")

if grade > 100 : 
    print(">Grade: impossible!")

#Task 18

number = int(input(">Enter number: "))

Cal1 = number%3
Cal2 = number%5

if Cal1 == 0 and Cal2 != 0:
    print(">Fizz")

if Cal1 != 0 and Cal2 == 0:
    print(">Buzz")

if Cal1 == 0 and Cal2 == 0:
    print(">FizzBuzz")

if Cal1 != 0 and Cal2 != 0:
    print(">Not Fizz or Buzz")

#Task 19

number = int(input("Please type in a number: "))

if number > 0 and number % 2 == 0:
    print(">The number is even")

if number > 0 and number % 2 != 0:
    print(">The number is odd")

if number < 0:
    print(">The number is negative or zero")

#Task 20

number = int(input("Please type in a number: "))

if number % 4 == 0:
    if number %100 != 0:
        print(">That year is a leap year.")
    else:
        if number % 400 == 0:
            print(">That year is a leap year.")
        else:
            print(">That year is not a leap year.")
else:
    print(">That year is not a leap year.")
