val1 = 10
val2 = 100
num = int(input("Please enter a number greater than 10 and less than 100"))
if num > val1 and num < val2:
    print (num)
elif num < val1:
    print ( num, "is too small!")
else:
    print ( num, "is too big!")
