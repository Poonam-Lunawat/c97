import random
print("\n Number guessing game \n You have 3 chances to guess the number.\n number ranges from 1 to 9")
number= random.randint(1,9)
chance=1

while chance<=3:
    userInput = int(input("Guess the number : "))
    if number<userInput:
        print("Worng, guess a number lower than this number")
    elif number>userInput:
        print("Worng, guess a number higher than this number")
    else:
        print("Congratulations you Won!!!")
        break
    chance+=1
if chance>3:
    print("You lost the number was: ",+number)
   