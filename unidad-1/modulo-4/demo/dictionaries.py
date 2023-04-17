#
# Un diccionario en Python es una colección desordenada de pares clave-valor.
#

# Crear un diccionario vacío
mi_diccionario = dict()
print("\nCrear un diccionario vacío (funcion):", mi_diccionario)

# Crear un diccionario vacío
mi_diccionario = {}
print("\nCrear un diccionario vacío (operador):", mi_diccionario)

# Crear un diccionario con elementos
mi_diccionario = dict({"clave1": "valor1", "clave2": "valor2"})
print("\nCrear un diccionario con elementos (funcion):", mi_diccionario)

# Crear un diccionario con elementos
mi_diccionario = {"clave1": "valor1", "clave2": "valor2"}
print("\nCrear un diccionario con elementos (operador):", mi_diccionario)

# Acceder a un valor del diccionario por su clave
valor = mi_diccionario["clave1"]
print("\nAcceder a un valor del diccionario por su clave:", valor)

# Modificar el valor de una clave en el diccionario
mi_diccionario["clave1"] = "nuevo_valor"
print("\nModificar el valor de una clave en el diccionario:", mi_diccionario)

# Agregar un nuevo par clave-valor al diccionario
mi_diccionario["clave3"] = "valor3"
print("\nAgregar un nuevo par clave-valor al diccionario:", mi_diccionario)

# Eliminar un par clave-valor del diccionario
del mi_diccionario["clave1"]
print("\nEliminar un par clave-valor del diccionario:", mi_diccionario)

# Obtener el número de elementos en el diccionario
longitud = len(mi_diccionario)
print("\nObtener el número de elementos en el diccionario:", longitud)

# Limpiar todos los elementos del diccionario
mi_diccionario.clear()
print("\nLimpiar todos los elementos del diccionario:", mi_diccionario)


#
# Puedo recorrer los elementos de las listas usando bucles
#

# Recorrer las claves de un diccionario con FOR
mi_diccionario = {
    "clave1": "valor1", 
    "clave2": "valor2", 
    "clave3": "valor3"}
print("\nRecorrer las claves de un diccionario con FOR:")
for clave in mi_diccionario:
    print(clave)

# Recorrer los valores de un diccionario con FOR
print("\nRecorrer los valores de un diccionario con FOR:")
for valor in mi_diccionario.values():
    print(valor)

# Recorrer los pares clave-valor de un diccionario con FOR
print("\nRecorrer los pares clave-valor de un diccionario con FOR:")
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}; Valor: {valor}")


#
# Puedo usar Operadores de Pertenencia, que devuelven un valor booelano y nos sirven para comprobar condiciones
#

# Comprobar si existe o no una clave dentro con el Operador de Pertenencia (IN y NOT IN)
existe = "clave3" in mi_diccionario
no_existe = "clave3" not in mi_diccionario
print("\nComprobar si existe o no una clave en el diccionario (IN):", existe)
print("Comprobar si existe o no una clave en el diccionario (NOT IN):", no_existe)

# Comprobar si existe o no una clave dentro con el Operador de Pertenencia (IN y NOT IN)
existe = "clave3" in mi_diccionario.keys()
no_existe = "clave3" not in mi_diccionario.keys()
print("\nComprobar si existe o no una clave en el diccionario (IN):", existe)
print("Comprobar si existe o no una clave en el diccionario (NOT IN):", no_existe)

# Comprobar si existe o no un valor dentro con el Operador de Pertenencia (IN y NOT IN)
existe = "valor3" in mi_diccionario.values()
no_existe = "valor3" not in mi_diccionario.values()
print("\nComprobar si existe o no un valor en el diccionario (IN):", existe)
print("Comprobar si existe o no un valor en el diccionario (NOT IN):", no_existe)


#
# Crear Diccionarios a partir de otras estructuras de datos
#

# Crear un diccionario a partir de dos listas
claves = ["clave1", "clave2", "clave3"]
valores = ["valor1", "valor2", "valor3"]
mi_diccionario = dict(zip(claves, valores))
print("\nCrear un diccionario a partir de dos listas:", mi_diccionario)

# Crear un diccionario a partir de una lista de tuplas
mi_diccionario = dict([("clave1", "valor1"), ("clave2", "valor2"), ("clave3", "valor3")])
print("\nCrear un diccionario a partir de una lista de tuplas:", mi_diccionario)

# Crear un diccionario con valores por defecto
mi_diccionario = dict.fromkeys(["clave1", "clave2", "clave3"], "valor_por_defecto")
print("\nCrear un diccionario con valores por defecto:", mi_diccionario)

# Obtener el valor de una clave en el diccionario con GET
valor = mi_diccionario.get("clave1")
print("\nObtener el valor de una clave en el diccionario con GET:", valor)

# Obtener el valor de una clave en el diccionario con GET y valor por defecto
valor = mi_diccionario.get("clave_inexistente", "valor_por_defecto")
print("\nObtener el valor de una clave en el diccionario con GET y valor por defecto:", valor)


#
# Tambien puedo crear un nuevo diccionario, mezclando dos o mas diccionarios previos
#

# Combinar dos diccionarios
diccionario1 = {"clave1": "valor1", "clave2": "valor2"}
diccionario2 = {"clave2": "valor2", "clave3": "valor3", "clave4": "valor4"}

# En Python 3.5 o anterior
diccionario_combinado = diccionario1.copy()
diccionario_combinado.update(diccionario2)
print("\nCombinar dos diccionarios (Python 3.5 o anterior):", diccionario_combinado)

# En Python 3.9 o posterior
diccionario_combinado = diccionario1 | diccionario2
print("\nCombinar dos diccionarios (Python 3.9 o posterior):", diccionario_combinado)