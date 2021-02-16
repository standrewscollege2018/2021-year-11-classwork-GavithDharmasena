#program that sets a number between 1 and 10 then gets the user to keep guessing the number

#importing random to generate the set number
import random

#constants
random_num = random.randint(1,100)
keep_guessing = True
play_again = True
count = 0
highscore = 0
new_highscore = 101

#guessing
while play_again == True:
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
                highscore = 101 - count
                if new_highscore >= highscore:
                    new_highscore = highscore
                    print ("Your highscore is",str(new_highscore),"/ 100")
                else:
                    print ("Your highscore is",str(highscore),"/ 100")
            #playing the game again
            play_again = input("Would you like to play again (yes or no)?: ")
            if play_again == "no":
                print("Ok, thanks for playing.")
                keep_guessing = False
        #higher/lower
        else:
            if random_num > guess:
                print("higher")
            else:
                print("lower")


