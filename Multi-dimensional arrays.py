# this program is for multi-dimensional arrays (lists in lists)
people = []
keep_asking = True


while keep_asking == True:
    name = input("what is your name?(enter done when you are finished): ")
    if name == "done":
        keep_asking = False
    else:
        try:
            age = int(input("What is your age?: "))
            people.append([name, age])
            print(people)
        except:
            print("INTEGER PLS")




for num in range(0,len(people)):
    print("{} is {} years old".format(people[num][0],people[num][1]))




