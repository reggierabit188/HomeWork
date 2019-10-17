def dog(a, b):
    gr = 1
    for i in range(abs(b)):
        gr *= a
    if b >= 0:
        return gr
    else:
        return 1 / gr


print(dog(float(input("Enter first num - ")), int(input("Enter secound num - "))))