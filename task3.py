a = int(input('a - '))
b = int(input('b - '))
c = int(input('c - '))
if a <= b <= c:
        x = b;
        y = c
if b < a < c:
        x = a;
        y = c
if c < a < b:
        x = a;
        y = b
print(x + y)