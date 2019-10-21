from functools import reduce
my_list = range (100, 1000)
new_list = [el for el in my_list if el % 2 == 0]

sum_all = reduce(lambda x, y: x + y, new_list)

print(sum_all)