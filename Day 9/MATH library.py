import math

num = 25
x = 5.7
y = 2

print("Square Root:", math.sqrt(num))
print("Power:", math.pow(2, 5))
print("Factorial:", math.factorial(5))
print("Absolute Value:", abs(-15))
print("Ceiling:", math.ceil(x))
print("Floor:", math.floor(x))
print("Truncate:", math.trunc(x))
print("Remainder:", math.remainder(10, 3))
print("GCD:", math.gcd(24, 36))
print("LCM:", math.lcm(12, 18))
print("Exponent (e^2):", math.exp(2))
print("Natural Log:", math.log(10))
print("Log Base 10:", math.log10(1000))
print("Log Base 2:", math.log2(16))
print("2^5:", math.pow(2, 5))
print("2 Raised to 5:", math.pow(2, y))

print("\nConstants")
print("Value of pi:", math.pi)
print("Value of e:", math.e)
print("Infinity:", math.inf)

print("\nTrigonometric Functions")
print("sin(30°):", math.sin(math.radians(30)))
print("cos(60°):", math.cos(math.radians(60)))
print("tan(45°):", math.tan(math.radians(45)))

print("\nInverse Trigonometric Functions")
print("asin(0.5):", math.degrees(math.asin(0.5)))
print("acos(0.5):", math.degrees(math.acos(0.5)))
print("atan(1):", math.degrees(math.atan(1)))

print("\nAngle Conversion")
print("180 degrees to radians:", math.radians(180))
print("3.14159 radians to degrees:", math.degrees(3.14159))

print("\nHypotenuse")
print("Hypotenuse of 3 and 4:", math.hypot(3, 4))