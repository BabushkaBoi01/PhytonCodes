PHYTON CODES
1.....x = input('Enter 2 digit number\n')
first = x[0]
second = x[1]
firstInt = int(first)
secondInt = int(second)
c = firstInt+secondInt
cStr = str(c)


print(first+" + "+second + " = "+cStr)


2.....BMI
weight = input("Enter your weight in Kg : ")
height = input("Enter your height in metres : ")
weightInt = int(weight)
heightInt = float(height)

heightSquared = heightInt**2
bmi = weightInt/heightSquared
bmiF = round(float(bmi),1)
bmiFStr = str(bmiF)

print("Your BMI is : "+bmiFStr)


3.....Days left to 90
age = input("Enter your current age : ")
years = 90 - int(age)
weeks = years * 52
days = years * 365
months = years * 12

print(f"You have {days} days, {weeks} weeks and {months} left")

4.....Tip calculator
print("Welcome to tip calculator")
bill = input("What was the bill? $")
per = input("What percentage do you want to tip? 10 ,12, or 15? ")
peo = input("How many people to split the bill? ")

tip = round((float(per)/100)*float(bill),2)
total = tip+float(bill)
each = round(total/float(peo),2)

print(f"Total : ${total}\nEach Person should pay : ${each} ")

5.....Even or Odd
x = input("Enter number\n")
if int(x) % 2 == 0:
    print(f"Number is Even")
else:
    print(f"Number is Odd")

6.....Treasure Island Game
print('''\
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to the treasure Island")
print("Your mission is to find the treasure")
quest1 = input("You are at a junction, do you want to go left or right? ").lower()
if quest1 == "left":
    quest2 = input("You have advanced to a lake, do you want to swin or wait for a boat? ").lower()
    if quest2 == "wait":
        print("You have advanced and now faced with the doors")
        quest3 = input("What door do you want to open?Red?Blue?Yellow? ").lower()
        if quest3 == "red":
            print("It was a room full of snakes, Game Over")
        elif quest3 == "yellow":
            print("Congratulations you made it to the Treasure, you win")
        elif quest3 == "blue":
            print("Wrong room ,Game Over")
        else:
            print("Pick a door")
    else:
        print("You got eaten by a crocodile, Game Over")
else:
    print("You fell into a hole, Game Over")

7.....Grade Calculator
print("Exam Grade Calculator")
name = input("Name of exam : ")
maxi = input("Max possible score : ")
yourScore = input("Your score? : ")

percentage = ((int(yourScore)/int(maxi))*100)

if percentage >= 90:
    print(f"You got {percentage}% which is an A+")
elif percentage >=80 and percentage <90:
    print(f"You got {percentage}% which is an A-")
elif percentage >=70 and percentage <80:
    print(f"You got {percentage}% which is a B")
elif percentage >=60 and percentage <70:
    print(f"You got {percentage}% which is a C")
elif percentage >=50 and percentage <60:
    print(f"You got {percentage}% which is a D")
elif percentage >= 0 and percentage <= 49:
    print(f"You got {percentage}% which is an F")
else:
    print("Enter a  valid grade")
    
8...Fun Animal game
exit=" "
animal = " "
while exit!= "yes" and exit !="exit":
#while animal != "cow" and animal != "sheep" and animal != "cat":
    animal = input("What animal do you want? ").lower()
    if animal == "cow":
        print("A cow goes mooo")
    elif animal == "sheep":
        print("A sheep goes bahhh")
    elif animal == "cat":
        print("A cat goes meowww")
    elif animal == "lion":
        print("A lion roars I think")
    else:
        print("oops..we don't have that, we are currently working on it")
    exit = input("Do you want to exit? ")
