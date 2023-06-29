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

try:
    man_file = open("man_data.txt", "w")
    other_file = open("other_data.txt", "w")

    print(man, file=man_file)
    print(other, file=other_file)

except FileNotFoundError:
    print("There are no such files")

finally:
    man_file.close()
    other_file.close()

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
