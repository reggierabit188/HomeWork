my_file = open("my_file.txt", "r")
num_lines = sum(1 for line in open ('my_file.txt'))
print(num_lines)

