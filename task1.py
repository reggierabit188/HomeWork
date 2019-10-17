def func(x, z):
    return x // z


x = int(input("Enter first values - "))
if x <= 0:
    x = int(print("Error, please repeat program "))

else:
    z = int(input("Enter secound values - "))
if z <= 0:
    print("Error, please repeat program ")
else:
    print(func(x, z))
