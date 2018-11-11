def prime():
    x = int(input("What is the limit of prime numbers that you want to see?"))
    for i in range (2, x+1):
        count = 0
        for j in range (2, i):
        # Made another array so that it can divide the number in the first array too see if it is prime and is
        # stops at i because if we are finding if 5 is a prime we divide up to 5 instead of 11 in our example.
            if (i%j != 0):
                count += 1
        if count == i-2:
            print (i)
            # Prime numbers will have a count 2 less than itself because the mod will only equal 0 with 1 and itself.
prime()
# Will print 2, 3, 5, 7, 11 if the user inputs 11.

def primefac():
    x = int(input("Prime factors for which number?"))
    for i in range (2, x+1):
        count = 0
        for j in range (2, i):
            if (i%j != 0):
                count += 1
        if count == i-2 and x%i == 0:
            print (i)
# Same code as before but with an additional condition that it has to be a factor of the user input
primefac()
# Will print 2, 13 if the user inputs 26

def lettergrade():
    x = int(input("What is your number grade?"))
    if x >= 90 and x <= 100:
        return ("A")
    elif x >= 80 and x <= 89:
        return ("B")
    elif x >= 70 and x <= 79:
        return ("C")
    elif x >= 60 and x <= 69:
        return ("D")
    elif x >= 0 and x <= 59:
        return ("F")
    else:
        return ("Invalid input!")

lettergrade()
# Will print A if the user inputs 100

def collatz():
    x = int(input("What number do you want to start with?"))
    print (x)
    while x > 1:
        if x%2 == 0:
            x = x/2
            print (x)
        else:
            x = (3*x)+1
            print (x)
# Divides by 2 if even, and multiply by 3 and adds 1 if it is odd.
collatz()
# Will print 10, 5, 16, 8, 4, 2, 1 if the user inputs 10