import random
number = random.randint(1,10)

while True :
    x = int(input(" guess a number: "))
    if x > number :
        print("decrease your guess")
    elif x < number :
        print("increase your number")
    elif x == number :
        print("your guess is correct")
        break

