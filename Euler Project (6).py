#code that finds the difference between the sum of the square of the first 100 numbers and the sum of the first 100 numbers squared
count = 0
for num in range(1,101):
    num = num ** num
    count = count + num
    print(count)

print(count)