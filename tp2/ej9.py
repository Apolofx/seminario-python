frase = '3s un het3rog74ma2021//))'
letras = [letra for letra in frase if not (letra.isalpha() and frase.count(letra) > 1)]
isHeterograma = len(letras) == len(frase)
print(isHeterograma)
