nombres_1 = """'Agustin',
 'Alan',
 'Andrés',
 'Ariadna',
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabián',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'María',
 'MATEO',
 'Matias',
 'Nicolás',
 'NICOLÁS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomás',
 'Ulises',
 'Yanina'"""
nombres_2 = """'Agustin',
 'AGUSTIN',
 'Agustín',
 'Ailen',
 'Alfredo',
 'Amalia',
 'Ariana',
 'Bautista',
 'Braian',
 'Carla',
 'CESAR',
 'Daniel',
 'Diego',
 'ELIANA',
 'Facundo',
 'Facundo',
 'Facundo',
 'Facundo',
 'Federico',
 'Federico',
 'Flavia',
 'Francisco',
 'Germán',
 'Guido',
 'GUSTAVO',
 'Hilario',
 'Ignacio',
 'IVAN',
 'Jimmy',
 'Joaquín',
 'Jose',
 'Josue',
 'JUAN',
 'Juan',
 'Laura',
 'LAURA',
 'Lautaro',
 'Lautaro',
 'Ludmila',
 'Marcos',
 'Marcos',
 'MARIANELA',
 'MARTIN',
 'MATEO',
 'Mateo',
 'Matias',
 'MAURO',
 'Maximiliano',
 'NESTOR',
 'Nicolas',
 'Pedro',
 'Ramiro',
 'Sofía',
 'Tobias',
 'Tomás',
 'Tomás',
 'Ulises',
 'Yanina'"""
lista_nombres_1 = [nombre.strip(" ,\'").lower() for nombre in nombres_1.splitlines()]
lista_nombres_2 = [nombre.strip(" ,\'").lower() for nombre in nombres_2.splitlines()]
lista_nombres_en_ambos = [nombre for nombre in lista_nombres_1 if nombre in lista_nombres_2]

#Elimino los duplicados
lista_nombres_sin_repetir = list(dict.fromkeys(lista_nombres_en_ambos))

#Otra forma de eliminar los duplicados
for nombre in lista_nombres_en_ambos:
    if lista_nombres_en_ambos.count(nombre) > 1:
        lista_nombres_en_ambos.remove(nombre)

print(lista_nombres_en_ambos)

eval1 = """81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74"""

eval2 = """30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10"""

lista_notas_1 = [int(nota.strip(" ").strip(",")) for nota in eval1.splitlines()]
lista_notas_2 = [int(nota.strip(" ").strip(",")) for nota in eval2.splitlines()]
datos_por_alumno = list(zip(lista_nombres_1, lista_notas_1, lista_notas_2))

total = []
for dato in datos_por_alumno:
    total.append(dato[1] + dato[2])

print(f"{'':>4}{'Nombre':<10}{'Eval1':^10}{'Eval2':^10}{'Total':^10}")
for dato in datos_por_alumno:
    i = datos_por_alumno.index(dato)
    print(f"{i:>3}{' '+ dato[0]:<10}{dato[1]:^10}{dato[2]:^10}{total[i]:>7}")
