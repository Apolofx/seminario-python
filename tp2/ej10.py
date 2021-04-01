import string
grupo_1 = (['A', 'E', 'I', 'O', 'U', 'L',' N', 'R', 'S', 'T' ],1)
grupo_2 = (['D', 'G'],2)
grupo_3 = (['B', 'C',' M', 'P'],3)
grupo_4 = (['F', 'H', 'V', 'W',' Y'],4)
grupo_5 = (['K'],5)
grupo_6 = (['J', 'X'],8)
grupo_7 = (['Q', 'Z'],10)

grupos = [grupo_1, grupo_2, grupo_3, grupo_4, grupo_5, grupo_6, grupo_7]

diccionarios = [dict.fromkeys(grupo[0], grupo[1]) for grupo in grupos]
diccionario = {}
for dicc in diccionarios:
    diccionario.update(dicc)
print(diccionario)

palabra = input("ingrese palabra: ").upper()
puntaje = 0
for letra in palabra:
    if (letra in string.ascii_letters):
        puntaje += diccionario[letra]

print(f'Puntaje total: {puntaje}')