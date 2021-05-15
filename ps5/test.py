check = 'a b   c'
words = check.split(' ')
while "" in words:
    words.remove("")

print(words)