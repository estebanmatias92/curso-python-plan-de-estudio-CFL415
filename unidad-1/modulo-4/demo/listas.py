#
# Una lista en Python es una colección ordenada de elementos que pueden ser de cualquier tipo.
#

# Crear una lista vacía
mi_lista = list()
print("\nCrear una lista vacía (funcion):", mi_lista)

# Crear una lista vacía
mi_lista = []
print("\nCrear una lista vacía (operador):", mi_lista)

# Crear una lista con elementos
mi_lista = list([1, 2, 3])
print("\nCrear una lista con elementos (funcion):", mi_lista)

# Crear una lista con elementos
mi_lista = [1, 2, 3]
print("\nCrear una lista con elementos (operador):", mi_lista)

# Agregar un elemento al final de la lista
mi_lista.append(4)
print("\nAgregar un elemento al final de la lista:", mi_lista)

# Insertar un elemento en una posición específica
mi_lista.insert(1, 5)
print("\nInsertar un elemento en una posición específica:", mi_lista)

# Extender la lista con otra lista
mi_lista.extend([6, 7])
print("\nExtender la lista con otra lista:", mi_lista)

# Acceder a un elemento de la lista por su índice
primer_elemento = mi_lista[0]
print("\nAcceder a un elemento de la lista por su índice:", primer_elemento)

# Eliminar un elemento de la lista por su índice
del mi_lista[1]
print("\nEliminar un elemento de la lista por su índice:", mi_lista)

# Eliminar un elemento de la lista por su valor
mi_lista.remove(3)
print("\nEliminar un elemento de la lista por su valor:", mi_lista)

# Eliminar y devolver el último elemento de la lista
ultimo_elemento = mi_lista.pop()
print("\nEliminar y devolver el último elemento de la lista:", ultimo_elemento)
print("Lista después de eliminar el último elemento:", mi_lista)

# Obtener el número de elementos en la lista
longitud = len(mi_lista)
print("\nObtener el número de elementos en la lista:", longitud)

# Obtener el índice de un elemento en la lista
indice = mi_lista.index(2)
print("\nObtener el índice de un elemento en la lista:", indice)

# Contar cuántas veces aparece un elemento en la lista
conteo = mi_lista.count(2)
print("\nContar cuántas veces aparece un elemento en la lista:", conteo)

# Ordenar la lista
mi_lista.sort()
print("\nOrdenar la lista:", mi_lista)

# Invertir el orden de la lista
mi_lista.reverse()
print("\nInvertir el orden de la lista:", mi_lista)

# Limpiar todos los elementos de la lista
mi_lista.clear()
print("\nLimpiar todos los elementos de la lista:", mi_lista)

# Convertir una Cadena de Caracteres (string) en una lista
mi_string = "Hola Mundo"
mi_lista = list(mi_string)
print("\nConvertir un string a lista:", mi_lista)
print("Convertir un string a lista (valor literal):", list("Juancito"))


#
# Puedo recorrer los elementos de las listas usando bucles
#

# Recorrer los elementos de una lista con FOR
print("\nRecorrer los elementos de una lista con FOR:")
for elemento in mi_lista:
    print(elemento)

# Recorrer los elementos de una lista con WHILE
print("\nRecorrer los elementos de una lista con WHILE:")
i = 0
longitud = len(mi_lista)
while (i < longitud):
    print(mi_lista[i])
    i += 1

# Recorrer los elementos de una lista con FOR
print("\nRecorrer los elementos e indices de una lista (ENUMERATE):")
for indice, elemento in enumerate(mi_lista):
    print(f"Indice: {indice}; Elemento: {elemento}")


#
# Puedo usar Operadores de Pertenencia, que devuelven un valor booelano y nos sirven para comprobar condiciones
#

# Comprobar si existe o no, un elemento dentro, con el Operador de Pertenencia (IN y NOT IN)
existe = "H" in mi_lista
no_existe = "H" not in mi_lista
print("\nComprobar si existe o no, un elemento en la lista (IN):", existe)
print("Comprobar si existe o no, un elemento en la lista (NOT IN):", no_existe)


#
# Tambien puedo obtener sub-listas, usando la sintaxis Slice 
#

# Obtener una porción de la lista
sub_lista = mi_lista[1:4]
print("\nObtener una porción de la lista:", sub_lista)

# Obtener una porción de la lista con un paso específico
sub_lista = mi_lista[1:6:2]
print("\nObtener una porción de la lista con un paso específico:", sub_lista)

# Obtener una porción de la lista desde el principio hasta un índice específico
sub_lista = mi_lista[:3]
print("\nObtener una porción de la lista desde el principio hasta un índice específico:", sub_lista)

# Obtener una porción de la lista desde un índice específico hasta el final
sub_lista = mi_lista[3:]
print("\nObtener una porción de la lista desde un índice específico hasta el final:", sub_lista)

# Invertir la lista
mi_lista_invertida = mi_lista[::-1]
print("\nInvertir la lista:", mi_lista_invertida)

# Crear una copia superficial de la lista
mi_lista_copia = mi_lista[:]
print("\nCrear una copia superficial de la lista:", mi_lista_copia)


#
# Concatenado y Replica de listas, tuplas, strings
#

# Concatenar dos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1 += lista2
lista_concatenada = lista1 + lista2
print("\nConcatenar dos listas:", lista_concatenada)

# Replicar una lista
mi_lista = [1, 2, 3]
lista_replicada = mi_lista * 3
print("\nReplicar una lista:", lista_replicada)
