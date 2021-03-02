#program for a computer inside a police patrol car
#constant for while loops
keep_asking = True

#storing tickets and wanted people
speeding_tickets = []
warrants = ["John Smith", "Helga Norman", "Zach Conroy",]


print ("Greetings.")
name = input("What is their name?(enter end to end the day): ")
#arrests
if name in warrants:
    print (name + "is wanted for arrest.")
#ending the day
elif name == "end":
    keep_asking = False

while keep_asking == True:
    #making sure it is an integer
    try:
        speed_limit = int(input("What is the speed limit?: "))
        speed = int(input("What is their speed?: "))

        if speed_limit > speed:
            print ("No fine")
        elif (speed - speed_limit) < 10:
            print ("$30 fine")
        elif (speed - speed_limit) > 9 and (speed - speed_limit) < 20:
            print ("$80 fine")
        elif (speed - speed_limit) > 19 and (speed - speed_limit) < 30:
            print ("$130 fine")
        elif (speed - speed_limit) > 29:
            print ("$180 fine")

    except:
        print ("That is not an integer")

