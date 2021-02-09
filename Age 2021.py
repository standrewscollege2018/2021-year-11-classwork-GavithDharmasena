#program that takes name and year of birth and prints their age

#constants
YEAR = 2021

#getting name and date of birth
name = str(input("What is your name?: "))
birth_date = int(input("When were you born?: "))

current_age = YEAR - birth_date
if birth_date > 0 and birth_date <= YEAR:
    print(name, "will turn",current_age, "in 2021.")
else:
    print("Invalid age, please re-etner.")

