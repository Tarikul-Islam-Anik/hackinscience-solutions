with open('words.txt') as f:
    words = f.read()

frequency = {}

for i in words:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

for i in frequency:
    print('{}: {:.2f}'.format(i, frequency[i]/(len(words))))
