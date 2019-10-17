def green(words):
    first_let_small = words[0]
    first_let_big = chr(ord(first_let_small) - ord('a') + ord('A'))
    return first_let_big + words[1:]


source = input("Enter anyone words - ").split()
res = []
for words in source:
    res.append(green(words))
print(' '.join(res)[:10])