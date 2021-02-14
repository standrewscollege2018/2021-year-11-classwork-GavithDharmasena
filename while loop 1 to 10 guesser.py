#program that sets a number between 1 and 10 then gets the user to keep guessing the number

#importing random to generate the set number
import random

#constants
random_num = random.randint(1,100)
keep_guessing = True
count = 0

#guessing
while keep_guessing == True:
    count += 1
    guess = int(input("Guess a number from 1 to 100: "))
    #showing guess is right
    if guess == random_num:
        print ("That's right!")
        #showing number of guesses
        if count == 1:
            print ("It only took you 1 guess")
        else:
            print ("It only took you",count,"guesses.")
        keep_guessing = False
    #higher/lower
    else:
        if random_num > guess:
            print("higher")
        else:
            print("lower")

