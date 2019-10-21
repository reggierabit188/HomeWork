ml = [1, 4 ,3 ,3, 1, 4, 5, 10]
def func(ml):
    for x in ml:
        if ml.count(x) == 1:
            yield x

res = [x for x in nodpl(ml)]
print(res)