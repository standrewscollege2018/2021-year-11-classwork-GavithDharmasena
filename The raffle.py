import random
import time

raffle_entrants = []
keep_asking = True
count = 0
sleep_time = 3
random = random.randint

print ("Greetings!")
prize = input("What is the prize of this raffle?: ")

while keep_asking == True:
    try:
        prize_value = int(input("What is the value of the prize?: "))
        keep_asking = False
    except:
        print ("Error, that is not an integer")

keep_asking = True
while keep_asking == True:
    count += 1
    if count < 2:
        names = input("Enter the first name: ")
        raffle_entrants.append(names)
        if names == "end":
            print("No entrants? No winner. I will take the",prize,"then.")
    else:
        names = input("Enter the next name: ")
        raffle_entrants.append(names)
        if names == "end":
            print("There are",len(raffle_entrants),"in this raffle and the prize is:" + prize)
            time.sleep(sleep_time)
            print ("and...")
            time.sleep(sleep_time)
            print ("the winner is...")
            time.sleep(sleep_time)
            print (raffle_entrants[random.randint(0,len(raffle_entrants))])