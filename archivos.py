

file=open('alumnos.txt', 'r')
nombres=file.readline()
print(nombres)
file.close()
for item in nombres:
    print(item, end='')