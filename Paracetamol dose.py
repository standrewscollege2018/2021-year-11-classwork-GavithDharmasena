#this program collects the age and weight of the user and suggests the correct 4-6 hourly paracetamol dosage

#constants
UNDER_12 = 12
CHILD_DOSE = 10


#getting user details
age = int(input("What is the patients age?: "))
weight = float(input("What is the patients weight?(kg): "))

while age > 0:
    if age < 12:
        print (CHILD_DOSE * weight, "mg is your recommended paracetamol dosage")
    else:
        print ("Two 500mg paracetamol tablets")
    break
else:
    print ("Invalid age")