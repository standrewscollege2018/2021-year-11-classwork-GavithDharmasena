#program that counts to asked number and prints fizz on 3x, buzz on 5x and fizzbuzz on 3x and 5x

#asking for number to count to
num = int(input("What number should we count to?: "))
num = num + 1

multiple1 = int(input("What is the first special multiple?: "))
multiple2 = int(input("What is the second special multiple?: "))

word1 = input("What is the first special word?: ")
word2 = input("What is the second special word?: ")

#printing fizz/buzz/fizzbuzz/number
for num in range(1,num):
    if num % multiple1 == 0 and num % multiple2 == 0:
        print(word1+word2)
    elif num % multiple1 == 0:
        print(word1)
    elif num % multiple2 == 0:
        print(word2)
    else:
        print(num)
print("All done!")