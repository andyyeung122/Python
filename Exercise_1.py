import math

minutes = int(input("Enter the minute:"))
seconds = int(input("Enter the seconds:"))

total_seconds = ((minutes * 60) + seconds)

print ("The total seconds is:", total_seconds)
#answer is 2562 seconds

r = float(input("Enter the radius:"))

volume_S = ((4/3) * math.pi * math.pow(r, 3))

print ("The volume is:", volume_S)

temperature_in_F = -40

temperature_in_C = ((temperature_in_F - 32) * (5/9))

print ("The temperature from Fahrenheit to Celsius is:", temperature_in_C)

volume_RP = (1 * 2 * 3)
volume_C = 1

amount_of_C = (volume_RP / volume_C)

print ("The amount of cube C that can fit in R is:", amount_of_C)
