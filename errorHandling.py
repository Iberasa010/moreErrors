# import os

man = []
other = []
try:
    data = open('sketch.txt')
    for line in data:
        try:
            (quien, dialogo) = line.split(':', 1)
            line = line.strip()
            if quien == 'Man':
                man.append(dialogo)
            elif quien == 'Other Man':
                other.append(dialogo)
        except ValueError:
            pass
    data.close()
except FileNotFoundError:
    print("There is no such file")

# Nuevo code
try:
    with open("man_data.txt", "w") as man_file:
        print(man, file=man_file)
    with open("other_data.txt", "w") as other_file:
        print(other, file=other_file)

except FileNotFoundError:
    print("There are no such files")

# same as below but there is error handling. If for some reason the file can not be open or read the proper
# way the correspondent error is handled. The latter one is just ignored, while the first one
# prints an error message if the file hasn't been found.


'''
if os.path.exists('sketch.txt'):
    data = open('sketch.txt')
    for line in data:
        if line.find(':') != -1:
            (quien, dialogo) = line.split(':', 1)
            print(quien, end='')
            print(' said: ', end='')
            print(dialogo, end='')
    data.close()
else:
    print("Such file does not exist")
'''

# The code above reads a file if found. There's no error handling because whether the file
# exists or not is checked beforehand

oso = open("osoPolar.txt", "w")
# ballena = open("ballena.txt" "w")
# print("Las ballenas son los mayores animales del planeta tierra", file=ballena)
print("Los osos polares son los mayores depredadores de tierra firme", file=oso)

oso.close()


# Duda que tenía antes. Efectivamente no puedes cerrar con un .close() algo no declarado.
# por tanto hay que hacer un if para que el finally no pete.

'''try:
    datados = open("missing.txt")
    print(datados.readline(), end='')
except FileNotFoundError as fileNotFound:
    print("No file has been found and a " + str(fileNotFound) + " error has occured")
finally:
    if 'datados' in locals():
        datados.close()

# hay mucha lógica extra que solapa el verdadero comportamiento del código.
# El try/except/finally es tan común que Python abstrae este patrón para hacerlo más simple.

try:
    with open("missing.txt") as datados:
        print(datados.readline(), end='')
except FileNotFoundError as err:
    print("Error: " + str(err)) '''
