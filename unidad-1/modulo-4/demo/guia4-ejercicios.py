#
# Listas (list)
#

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

# Mostrar

# Actualizar

# Borrar



#
# Diccionario (dict)
#

# Crear

# Mostrar

# Actualizar

# Borrar



#
# Conjunto (set)
#

# Crear

# Mostrar

# Actualizar

# Borrar


