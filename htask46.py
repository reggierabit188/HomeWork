from itertools import count

for el in count(8):
    print(el)
-------------------------------
from itertools import cycle

с = 0
for el in cycle(1):
    if с > 8:
        break
    print(el)
    с += 1