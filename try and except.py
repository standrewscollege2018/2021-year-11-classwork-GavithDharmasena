keep_asking = True
while keep_asking == True:
    try:
        num = int(input("Enter a whole number: "))
        print (num)
        keep_asking = False
    except:
        print("That is not a whole number please re-enter the number")
