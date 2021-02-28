keep_asking = True
names = ["John", "Paul", "Cringer",]

while keep_asking == True:
    name = input("Enter a name: ")

    if name in names:
        print ("You're on the list")
        keep_asking = False
    else:
        print ("You're not on the list")