def func(a, b):
    return int(a) + int(b)


a1 = input("Enter - ")
a2 = input("Enter - ")
a3 = input("Enter - ")

n = [a1, a2, a3]
n.sort()
n.pop(0)
a = n[0]
b = n[1]
print(func(a, b))