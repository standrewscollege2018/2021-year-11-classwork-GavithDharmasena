#code that find the largest palindromic numbers that is a multiple of 2 3-digit numbers
n = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                 n = a * b
                 print (n)


print(n,"is the largest palindromic that is the product of two 3 digit numbers")