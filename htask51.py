first_file = open("my_file.txt", "w")
text = input('Enter anyone text - ')
text = first_file.write(text)

while True:
    text = input()
    if text:
        first_file.append(text)
    else:
        break

first_file.close()