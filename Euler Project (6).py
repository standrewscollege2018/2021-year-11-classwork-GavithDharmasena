#code that finds the difference between the sum of the square of the first 100 numbers and the sum of the first 100 numbers squared
count = 0
square_num = 0
for num in range(1,101):
    square_num = num ** 2
    count = count + square_num
    print (square_num)

print (count)