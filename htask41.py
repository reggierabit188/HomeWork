from sys import argv

name, payment, prize = argv
production = int(input("Production on day - "))

x = int(payment)
y = int(prize)

if production <= 8:
    def pay_cals():
        return production * x
else:
    def pay_cals():
        return 8 * x + y * (production - 8)

print(pay_cals())