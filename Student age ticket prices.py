#program that takes ages and gives prices according to ages and students


age = int(input("how old are you?: "))

if age >= 5 and age < 13:
    print("Your ticket costs $7")
elif age >= 13 and age < 18:
    student = int(input("Are you a student? 1 for yes and 0 for no: "))
    if student is 1:
        print("Your ticket costs $8")
    else:
        print("Your ticket costs $9")
elif age >= 18:
    print("Your ticket costs $12")
else:
    print("You go free!")
