#this program takes an exam mark and prints the grade accordingly

#constants are the grade boundaries
A_GRADE = 90
B_GRADE = 70
C_GRADE = 50

#geting user's mark
mark = int(input("What is your exam mark?: "))

#printing the right grade accoriding to user's mark
if mark >= A_GRADE:
    print("You achieved an A on your exam, well done!")
elif mark >= B_GRADE:
    print("You achieved a B on your exam, good job!")
elif mark >= C_GRADE:
    print("You achieved a C on your exam")
else:
    print("You failed your exam :(")

#showing the program has ended
print("")
print("This is the end of the program.")


