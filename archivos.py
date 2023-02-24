"""
r= leer
w=escribir
a= adiciona contenido al archivo

file=open('alumnos.txt','w')
nombres=file.readline()
print(nombres)
file.close()"""
"""
for item in nombres:
    print(item,end='')
"""

file=open('alumnos2.txt', 'a')
file.write('\n' + 'Hola mundo!!!!!!')
file.write('\n' + 'Hola mundo2!!!!!!')
file.close()
#for item in nombres:
   # print(item, end='')