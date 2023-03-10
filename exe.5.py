original = input('digite uma palavra para ser invertida: ')
invertida = ''
for i in range(len(original) - 1, -1, -1):
    invertida += original[i]

print(invertida)
