#program that asks the user for two numbers, prints them says the larger and prints the total

#making sure the number is an integer
try:
    #getting the numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    #logic for prints
    if num1 > num2:
        print ("Your numbers are:",num1,"and",num2,)
        print (num1,"is the largest number")
        print ("The total is:",num1 + num2,)
    elif num2 > num1:
        print ("Your numbers are:",num1,"and",num2,)
        print (num2,"is the largest number")
        print ("The total is:",num1 + num2,)
    else:
        print ("Your numbers are:",num1,"and",num2,)
        print (num1,"and",num2,"are the same size")
        print ("The total is:",num1 + num2,)
except:
    print ("Error, not a whole number.")