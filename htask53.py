def data_to_file(file):
    dct = []
    print('')
    with open(file, 'w') as f:
        while True:
            sname = input('Фамилия:')
            wage = input('Зп:')
            if sname:
                f.write(f'{sname} : {float(wage)}\n')
            else:
                break

def read_txt(file):
    salary = []
    with open(file) as f:
        lines = f.readlines()
    for i in lines:
        i = i.split(' : ')
        salary.append(i)
    return dict(salary)

def my_stat(dct):
    print('меньше 20:')
    for sname, wage in dct.items():
        if float(wage) < 20000:
            print(sname)
    print(f'\nсредняя: {sum([float(x) for x in dct.values()]) / len(dct)}')

data_to_file('my_file.txt')
my_stat(read_txt('my_file.txt'))