data = open('sketch.txt')

frase = "Casi la cago bien cagada Julio"

print(frase.find(":"))


data.seek(0)
for line in data:
    if line.find(':') != -1:
        (quien, dialogo) = line.split(':', 1)
        print(quien, end='')
        print(' said: ', end='')
        print(dialogo, end='')

data.close()


'''Problemas: ¿Vas a hacer un if para cada posible error que tengas? Qué
ocurre con los archivos más grandes? Vas a ejecutarlos hasta que después de 1000 intentos ya
no te den más errores? Tiene que haber algún modo de quitarnos de ifs, porque en este
tipo de ficheros simples funciona, pero en algunos más grandes no va a funcionar pero ni d coña.'''
