#program for a computer inside a police patrol car
#constants for while loops
keep_asking = True
keep_asking2 = True

#storing tickets and wanted people
names = []
speeding_fines = []
warrants = ["John Smith", "Helga Norman", "Zach Conroy",]


print ("Greetings.")
while keep_asking == True:
    name = input("What is their name?(enter end to end the day): ")
    #arrests
    if name in warrants:
        print (name + " is wanted for arrest, onto the next person please.")
    #ending the day
    elif name == "end":
        keep_asking = False
    #making sure it is an integer
    else:
        names.append(name)
        keep_asking2 = True
        while keep_asking2 == True:
            try:
                speed_limit = int(input("What is the speed limit?: "))
                speed = int(input("What is their speed?: "))
                keep_asking2 = False
                if speed_limit > speed:
                    print ("No fine")
                    speeding_fines.append("No fine")
                elif (speed - speed_limit) < 10:
                    print ("$30 fine")
                    speeding_fines.append("$30 fine")
                elif (speed - speed_limit) > 9 and (speed - speed_limit) < 20:
                    print ("$80 fine")
                    speeding_fines.append("$80 fine")
                elif (speed - speed_limit) > 19 and (speed - speed_limit) < 30:
                    print ("$130 fine")
                    speeding_fines.append("$130 fine")
                elif (speed - speed_limit) > 29:
                    print ("$180 fine")
                    speeding_fines.append("$180 fine")
            except:
                print ("That is not an integer")

for num in range(0,len(names)):
    print("{} with a {}".format(names[num],speeding_fines[num]))