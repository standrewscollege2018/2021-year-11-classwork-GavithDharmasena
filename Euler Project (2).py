#code that finds the sum of all even fibonnaci sequence numbers below 4000000
fib = 1
fib2 = 2
count = 0
total = 0

while count <=4000000:
    count = fib2
    if count % 2 == 0:
        total += count
    count = fib + fib2
    fib = fib2
    fib2 = count

print (total)



