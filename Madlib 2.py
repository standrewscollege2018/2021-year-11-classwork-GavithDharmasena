#this is a code that writes a madlib story using inputs from the user

#importing time for sleeps
import time

#getting details
name = input("Enter a name")
weapon = input("Enter a cool weapon")
monster = input("Enter a monster")
martial_art = input("Enter a martial art (or a made up one i.e. firebreathing)")


#writing the madlib story with prints
print ("Welcome to my secret lair {}, I see you have finally found the {} but even with the {} you are still no match for the {}.".format(name, weapon, weapon, monster))

#slowing down the story to give the reader time to read certain parts and give suspense
time.sleep(11)
print("And even if you do somehow make it past the {} I have mastered the art of {} MWUHAHHHAAHA!".format(monster, martial_art))