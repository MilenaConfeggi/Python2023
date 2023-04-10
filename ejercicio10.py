
nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


def InsisoA(nombres, notas_1, notas_2):
   nomynotas = zip(nombres.split(","), notas_1, notas_2)
   diccionario = {nom: (nota1, nota2) for nom, nota1, nota2 in nomynotas}
   return diccionario

def InsisoB (dicci):
    promedios = dict()
    for elem in dicci:
        promedios[elem] = sum(dicci[elem]) / len(dicci[elem])
    return promedios

def InsisoC (promedios):
    return sum(promedios.values())/(len(promedios))

def InsisoD (promedios):
    return max (promedios.items(), key= lambda estudiante: estudiante[1])[0]

def InsisoE (diccialumnos):  
    return min(diccialumnos.items(), key = lambda estudiante: estudiante[1])[0]

nombres = nombres.replace("\n", "")
diccialumnos = InsisoA(nombres, notas_1, notas_2)
print (diccialumnos)
promedios = InsisoB(diccialumnos)
print (promedios)
print ("El promedio general es de: ", InsisoC(promedios))
print ("El estudiante con mayor promedio es: ", InsisoD(promedios))
print ("El estudiante con la nota mas baja es: ", InsisoE(diccialumnos))