#program that takes 3 names and puts them in  list, then prints the list

names = []
count = 0
count2 = 0
keep_asking = True

while keep_asking == True:
    try:
        num_names = int(input("How many names do you want to enter? "))
        keep_asking = False
    except:
        print ("Please enter an integer.")

for i in range (0,num_names):
    count += 1
    if count < 2:
        name = input("Enter a name ")
        names.append(name)
    else:
        name = input("Enter another name ")
        names.append(name)


for i in range(0,num_names):
    print(count2+1, names[count2])
    count2 += 1
