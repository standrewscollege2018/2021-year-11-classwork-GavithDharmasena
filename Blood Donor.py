#Program to asses if the user could be a potential blood donor

#constants
DONOR_AGE = 16
DONOR_WEIGHT = 50

#getting user age and weight
age = int(input("What is your age?: "))
weight = float(input("What is your weight?(kg): "))

#checking user details with constants and printing accordingly
if age >= DONOR_AGE and weight >= DONOR_WEIGHT:
    print("You are an eligible blood donor.")
else:
    print("You are not an eligible blood donor.")

print("")
print("This is the end of the program.")