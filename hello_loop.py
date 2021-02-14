#program that takes an asked number of names and says hello to them

#getting number of people
number_names = int(input("How many names do you wish to enter?"))

#saying "Hello"
for num in range(0,number_names):
    name = input("Please enter a name: ")
    print("Hello",name)