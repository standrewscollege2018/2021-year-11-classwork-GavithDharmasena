#while loops

#constants
keep_asking = True

#asking name
while keep_asking == True:
    name = input("Enter you name: ")
    if name == "cringer":
        keep_asking = False
    else:
        print("wrong name")

print("Hi cringer")