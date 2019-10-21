my_list = [1, 3, 4, 5, 8]
new_list = [el for el in my_list]
for el in range(1, len(my_list)):
    if my_list[el] > my_list[el - 1]:
        print(my_list[el])