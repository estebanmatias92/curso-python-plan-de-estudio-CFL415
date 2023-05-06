#
# Listas (list)
#
"""
# Crear
mi_lista = ["Rojo", "Verde", "Azul"]



# Mostrar elemento
print("\nPrimer elemento:", mi_lista[0])                        # "Rojo"
print("Segundo elemento:", mi_lista[1])                         # "Verde"
print("Tercer elemento:", mi_lista[2])                          # "Azul"
print("Ultimo elemento:", mi_lista[-1])                         # "Azul"



# Mostrar toda la lista
print("")
for color in mi_lista:
    print("Color:", color)

# Forma dificil
print("")
tamaño = len(mi_lista)
for i in range(0, tamaño):
    print("Color:", mi_lista[i])



# Añadir elemento
mi_lista.append("Amarillo")
print("\nNuevo ultimo elemento: ", mi_lista[-1])                                             # "Amarillo"



# Añadir una lista de elementos
mi_lista.extend(["Marron", "Violeta", "Celeste"])
mi_lista += ["Naranja", "Rosa"]
print("")
for color in mi_lista:
    print("Color:", color)



# Borrar elemento
mi_lista.remove("Marron")
del mi_lista[-1]
print("")
for color in mi_lista:
    print("Color:", color)



# Borrar lista
mi_lista.clear()
print("")
print(mi_lista)

#
# Tupla (tuple)
#

# Crear
mi_tupla = ("Argentina", "Noruega", "Tailandia", "Australia", "Argentina")


# Mostrar elemento
print("\nPrimer elemento:", mi_tupla[0])                        # "Argentina"
print("Segundo elemento:", mi_tupla[1])                         # "Noruega"
print("Tercer elemento:", mi_tupla[2])                          # "Tailandia"
print("Ultimo elemento:", mi_tupla[-1])                         # "Australia"

# Mostrar 2

print("\nVeces repetido Argentina:", mi_tupla.count("Argentina"))

# Mostrar 3

print("")
for elemento in mi_tupla:
    print(f"Pais: {elemento}")

"""

#
# Diccionario (dict)
#

# Crear
mi_diccionario = {
    "Nombre": "Matias", 
    "Edad": 30,
    "Es estudiante": True
    }


# Mostrar
print(f"Mostrando Nombre: {mi_diccionario['Nombre']}")                  # Matias
print(f"Mostrando Edad: {mi_diccionario['Edad']}")                      # 30
print(f"Mostrando Es estudiante: {mi_diccionario['Es estudiante']}")    # True


for valor in mi_diccionario.keys():
    print(f"Valor es: {valor}")

# Actualizar
print("")
mi_diccionario["Lenguajes"] = ["python", "sql", "ruby", "c", "c++", "php", "javascript", "html", "css"]
for clave, valor in mi_diccionario.items():
    print(f"{clave} : {valor}")



# Borrar
print("")
del mi_diccionario["Lenguajes"]
for clave, valor in mi_diccionario.items():
    print(f"{clave} : {valor}")


mi_diccionario.clear()

print("")
print(mi_diccionario)

#
# Conjunto (set)
#

# Crear
mi_conjunto = {"Matias", 30, True}

print(mi_conjunto)

# Mostrar

# Actualizar

# Borrar

