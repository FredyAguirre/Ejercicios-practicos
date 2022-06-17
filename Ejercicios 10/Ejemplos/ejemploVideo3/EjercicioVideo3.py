archivo = open('estudiantes.txt','r')
tabla = []
for renglon in archivo:
    datos = renglon.split(', ')
    nom = datos[0]
    ape = datos[1]
    sexo = datos[2]
    doc = int(datos[3])
    edad = int(datos[4])
    est = float(datos[5])
    prom = float(datos[6])
    estudiante = [nom, ape, sexo, doc, edad, est, prom]
    tabla.append(estudiante)
archivo.close()

tabla.sort(key = lambda x: x[6], reverse = True)
print('Documento\tPromedio\tNombre completo')
for e in tabla:
    print(e[3], e[6], e[0]+' '+e[1], sep='\t\t')

promedio, baloncesto, menores = 0, 0, 0
for e in tabla:
    promedio += e[6]
    if e[2] == 'F' and e[5] >=1.8:
        baloncesto +=1
    if e[2] == 'M' and e[4] < 18:
        menores +=1
promedio = round(promedio/len(tabla),2)
print('\nPromedio general:', promedio)
print('Candidatas equipo baloncesto:', baloncesto)
print('Hombres menores de edad:', menores)
