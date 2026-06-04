num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)


# Palindrome Number Program

num = int(input("Enter a number: "))
temp = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if temp == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
#buzz number
num = int(input("Enter a number: "))

if num % 7 == 0 or num % 10 == 7:
    print("Buzz Number")
else:
    print("Not a Buzz Number")
n = int(input("Enter number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#perfect number

num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

#storng number

num = int(input("Enter a number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    fact = 1

    for i in range(1, digit + 1):
        fact *= i

    sum += fact
    num //= 10

if sum == temp:
    print("Strong Number")
else:
    print("Not a Strong Number")

#happy number

num = int(input("Enter a number: "))

while num != 1 and num != 4:
    sum = 0

    while num > 0:
        digit = num % 10
        sum += digit * digit
        num //= 10

    num = sum

if num == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")

#prime number

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not a Prime Number")

#armstorng number

num = int(input("Enter a number: "))
temp = num

digits = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** digits
    num //= 10

if sum == temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


































