def func(y, z):
    return y // z

a = int(input("Enter first values - "))
if y <= 0:
    y = int(print("Делить на нуль нельзя "))
else:
    z = int(input("Enter second values - "))
if z <= 0:
    print("Делить на нуль нельзя ")
else:
    print(func(y, z))