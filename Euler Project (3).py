#code that finds the largest prime number in 600851475143
prime_numbers = []

n = 600851475143

for num in range (2,775146):
    if n % num ==0:
        prime_numbers.append(num)
        print(num)


print (prime_numbers,"are all the factors of 600851475143")