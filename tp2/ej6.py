frase = """Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple."""
frase_en_minuscula = frase.lower()
lista_palabras_con_duplicados = frase_en_minuscula.replace("\n"," ").split(" ")
# Elimino duplicadas
lista_palabras = list(dict.fromkeys(lista_palabras_con_duplicados))
print(f"Usando dict.fromkeys:\n {lista_palabras}")

# Como no importa el orden, tambien podria crear una lista del set de palabras.
lista_palabras = list(set(lista_palabras_con_duplicados)) 
print(f"Usando un set:\n {lista_palabras}")
