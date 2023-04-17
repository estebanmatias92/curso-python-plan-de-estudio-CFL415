#
# Un conjunto (set) en Python es una colección desordenada de elementos únicos.
#

# Crear un conjunto vacío
mi_conjunto = set()
print("\nCrear un conjunto vacío:", mi_conjunto)

# Crear un conjunto con elementos
mi_conjunto = set([1, 2, 3])
mi_conjunto2 = {1, 2, 3}
print("\nCrear un conjunto con elementos (operador):", mi_conjunto)
print("Crear un conjunto con elementos (funcion):", mi_conjunto2)

# Agregar un elemento al conjunto
mi_conjunto.add(4)
print("\nAgregar un elemento al conjunto:", mi_conjunto)

# Agregar varios elementos al conjunto
mi_conjunto.update([5, 6])
print("\nAgregar varios elementos al conjunto:", mi_conjunto)

# Eliminar un elemento del conjunto
mi_conjunto.discard(3)
print("\nEliminar un elemento del conjunto:", mi_conjunto)

# Eliminar y devolver un elemento del conjunto
elemento = mi_conjunto.pop()
print("\nEliminar y devolver un elemento del conjunto:", elemento)
print("Conjunto después de eliminar el elemento:", mi_conjunto)

# Obtener el número de elementos en el conjunto
longitud = len(mi_conjunto)
print("\nObtener el número de elementos en el conjunto:", longitud)


#
# Puedo usar Operadores de Pertenencia, que devuelven un valor booelano y nos sirven para comprobar condiciones
#

# Comprobar si existe o no un elemento dentro con el Operador de Pertenencia (IN y NOT IN)
existe = 2 in mi_conjunto
no_existe = 2 not in mi_conjunto
print("\nComprobar si existe o no un elemento en el conjunto (IN):", existe)
print("Comprobar si existe o no un elemento en el conjunto (NOT IN):", no_existe)

# Limpiar todos los elementos del conjunto
mi_conjunto.clear()
print("\nLimpiar todos los elementos del conjunto:", mi_conjunto)

# Convertir una Cadena de Caracteres (string) en un conjunto
mi_string = "Hola Mundo"
mi_conjunto = set(mi_string)
print("\nConvertir un string a conjunto:", mi_conjunto)


#
# Puedo recorrer los elementos de las listas usando bucles
#

# Recorrer los elementos de un conjunto con FOR
print("\nRecorrer los elementos de un conjunto con FOR:")
for elemento in mi_conjunto:
    print(elemento)


#
# Puedo obtener uniones, diferencias e intersecciones entre conjuntos.
#

# Unión de conjuntos, suma de ambos conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
conjunto_union = conjunto1.union(conjunto2)
print("\nUnión de conjuntos:", conjunto_union)
print("Unión de conjuntos:", (conjunto1 | conjunto2))

# Intersección de conjuntos, elementos comunes entre ambos
conjunto_interseccion = conjunto1.intersection(conjunto2)
print("\nIntersección de conjuntos:", conjunto_interseccion)
print("Intersección de conjuntos:", conjunto1 & conjunto2)

# Diferencia entre los conjuntos, del primero con respecto al segundo y luego viceversa
conjunto_diferencia = conjunto1.difference(conjunto2)
print("\nDiferencia del primer conjunto con el segundo:", conjunto_diferencia)
print("Diferencia del segundo conjunto con el primero:", conjunto2 - conjunto1)

# Diferencia simétrica de conjuntos, elementos que no son cumunes entre ambos
conjunto_diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print("\nDiferencia simétrica de conjuntos:", conjunto_diferencia_simetrica)
print("Diferencia simétrica de conjuntos:", conjunto1 ^ conjunto2)

# Comprobar si un conjunto es subconjunto de otro
conjunto1 = {1, 2}
conjunto2 = {1, 2, 3}
es_subconjunto = conjunto1.issubset(conjunto2)
print("\nComprobar si un conjunto es subconjunto de otro:", es_subconjunto)

# Comprobar si un conjunto es superconjunto de otro
es_superconjunto = conjunto2.issuperset(conjunto1)
print("\nComprobar si un conjunto es superconjunto de otro:", es_superconjunto)