#
# Una tupla en Python es una colección ordenada e inmutable de elementos que pueden ser de cualquier tipo.
#

# Crear una tupla vacía
mi_tupla = tuple()
print("\nCrear una tupla vacía (funcion):", mi_tupla)

# Crear una tupla vacía
mi_tupla = ()
print("\nCrear una tupla vacía (operador):", mi_tupla)

# Crear una tupla con elementos
mi_tupla = tuple([1, 2, 3])
print("\nCrear una tupla con elementos (funcion):", mi_tupla)

# Crear una tupla con elementos
mi_tupla = (1, 2, 3)
print("\nCrear una tupla con elementos (operador):", mi_tupla)

# Acceder a un elemento de la tupla por su índice
primer_elemento = mi_tupla[0]
print("\nAcceder a un elemento de la tupla por su índice:", primer_elemento)

# Obtener el número de elementos en la tupla
longitud = len(mi_tupla)
print("\nObtener el número de elementos en la tupla:", longitud)

# Obtener el índice de un elemento en la tupla
indice = mi_tupla.index(2)
print("\nObtener el índice de un elemento en la tupla:", indice)

# Contar cuántas veces aparece un elemento en la tupla
conteo = mi_tupla.count(2)
print("\nContar cuántas veces aparece un elemento en la tupla:", conteo)

# Convertir una Cadena de Caracteres (string) en una tupla
mi_string = "Hola Mundo"
mi_tupla = tuple(mi_string)
print("\nConvertir un string a tupla:", mi_tupla)


#
# Puedo recorrer los elementos de las tuplas usando bucles
#

# Recorrer los elementos de una tupla con FOR
print("\nRecorrer los elementos de una tupla con FOR:")
for elemento in mi_tupla:
    print(elemento)

# Recorrer los elementos de una tupla con WHILE
print("\nRecorrer los elementos de una tupla con WHILE:")
i = 0
longitud = len(mi_tupla)
while (i < longitud):
    print(mi_tupla[i])
    i += 1

# Recorrer los elementos e índices de una tupla con ENUMERATE
print("\nRecorrer los elementos e índices de una tupla (ENUMERATE):")
for indice, elemento in enumerate(mi_tupla):
    print(f"Índice: {indice}; Elemento: {elemento}")


#
# Puedo usar Operadores de Pertenencia, que devuelven un valor booelano y nos sirven para comprobar condiciones
#

# Comprobar si existe o no un elemento dentro con el Operador de Pertenencia (IN y NOT IN)
existe = "H" in mi_tupla
no_existe = "H" not in mi_tupla
print("\nComprobar si existe o no un elemento en la tupla (IN):", existe)
print("Comprobar si existe o no un elemento en la tupla (NOT IN):", no_existe)


#
# Tambien puedo obtener sub-tuplas, usando la sintaxis Slice 
#

# Obtener una porción de la tupla
sub_tupla = mi_tupla[1:4]
print("\nObtener una porción de la tupla:", sub_tupla)

# Obtener una porción de la tupla con un paso específico
sub_tupla = mi_tupla[1:6:2]
print("\nObtener una porción de la tupla con un paso específico:", sub_tupla)

# Obtener una porción de la tupla desde el principio hasta un índice específico
sub_tupla = mi_tupla[:3]
print("\nObtener una porción de la tupla desde el principio hasta un índice específico:", sub_tupla)

# Obtener una porción de la tupla desde un índice específico hasta el final
sub_tupla = mi_tupla[3:]
print("\nObtener una porción de la tupla desde un índice específico hasta el final:", sub_tupla)

# Invertir la tupla
mi_tupla_invertida = mi_tupla[::-1]
print("\nInvertir la tupla:", mi_tupla_invertida)

# Crear una copia superficial de la tupla
mi_tupla_copia = mi_tupla[:]
print("\nCrear una copia superficial de la tupla:", mi_tupla_copia)


#
# Concatenado y Replica de listas, tuplas, strings
#

# Concatenar dos tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla1 += tupla2
tupla_concatenada = tupla1 + tupla2
print("\nConcatenar dos tuplas:", tupla_concatenada)

# Replicar una tupla
mi_tupla = (1, 2, 3)
tupla_replicada = mi_tupla * 3
print("\nReplicar una tupla:", tupla_replicada)