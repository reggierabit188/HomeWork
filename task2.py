def profile(**my_dict):
    return my_dict
i = 0
while  i < 5:
    name = input('Enter name: ')
    if name == " ": continue
    i += 1
    surname = input('Enter surname: ')
    if surname == " ": continue
    i += 1
    age = input('Enter year: ')
    if age == " ": continue
    i += 1
    city = input('Enter City of birth: ')
    if city == " ": continue
    i += 1
    phone = int(input('Enter Phone№: '))
    if phone == " ": continue
    i += 1
    email = input('Enter Email: ')
    if email == " ": continue
    my_dict = {'Username': name, 'Surname': surname, 'Year of birth': age, 'City of birth': city, 'Phone': phone,
           'Email': email}
print(profile(**my_dict))
