import math

a = 6
b = -5
c = 1

delta = b**2 - 4*a*c

if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")
else:
    print("Moadel rishe haqiqi nadarad.")
