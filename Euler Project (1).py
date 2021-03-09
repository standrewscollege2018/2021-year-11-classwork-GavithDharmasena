#code that finds the total of all multiples of 3 or 5 below 1000
x = 0

for num in range(0,1000):
    if num % 3 == 0 or num % 5 == 0:
        x = x + num


print (x)