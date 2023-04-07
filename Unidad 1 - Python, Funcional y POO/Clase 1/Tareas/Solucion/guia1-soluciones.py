import os

#
# Ejercicio 1
#
print("\n\nPidiendo Datos")
#mi_nombre = "Matias Lapenta"
mi_nombre = input("Ingrese su nombre: ")                        # Pido por consola al usuario que ingrese un valor alfabetico



#
# Ejercicio 2
#
#mi_edad = 30
mi_edad = int(input("Ingrese su edad: "))                       # Pido por consola al usuario, que ingrese un valor entero



#
# Ejercicio 3
#
#mi_altura = 1.64
mi_altura = float(input("Ingrese su altura: "))                 # Pido por consola al usuario, que ingrese un valor decimal



#
# Ejercicio 4
#
#soy_estudiante = False
soy_estudiante = bool(int(input("Es estudiante? (1/0): ")))     # Pido por consola al usuario, que ingrese un valor booleano (1/0)



#
# Ejercicio 5
#
print("\nMostrando Datos")
print(f"Mi nombre:\t{mi_nombre}")                               # Muestro el valor de lo ingresado por el usuario
print(f"Mi edad:\t{mi_edad} años")
print(f"Mi altura:\t{mi_altura} metros")
print(f"Es estudiante?:\t{soy_estudiante}")


#
# Ejercicio 6
#
print("\nTipos")
print(f"mi_nombre:\t{type(mi_nombre)}")                         # Muestro cada tipo de dato, llamando a type() y pasandole como argumento mis variables anteriores
print(f"mi_edad:\t{type(mi_edad)}")
print(f"mi_altura:\t{type(mi_altura)}")
print(f"soy_estudiante:\t{type(soy_estudiante)}")


#
# Ejercicio 7
#
print("\n\nPidiendo Datos")
#mi_peso = 70
mi_peso = float(input("Ingrese su peso: "))                     # Pido un valor decimal por consola y guardo lo que el usuario ingrese, en una variable

print("\nMostrando Datos")
print(f"Mi peso:\t\t{mi_peso}Kg")                               # Muestro ese valor por pantalla



#
# Ejercicio 8
#
mi_IMC = (mi_peso / (mi_altura ** 2))                           # Hago la operacion aritmetica y guardo el resultado en la variable

print(f"Mi IMC:\t\t\t{mi_IMC}")                                 # Muestro el resultado



#
# Ejercicio 9
#
mi_IMC_redondeado = round(mi_IMC)                               # Llamo a la funcion de redondeo decimal y guardo el resultado en la variable

print(f"Mi IMC redondeado:\t{mi_IMC_redondeado}")               # Muestro el resultado



#
# Ejercicio 10
#
edad_en_5_años = mi_edad + 5                                    # Hago la operacion aritmetica y guardo el resultado en la variable

print("\n\nMostrando Datos")
print(f"Mi edad en 5 años:\t\t{edad_en_5_años} años")           # Muestro el resultado




#
# Ejercicio 11
#   
dias_vivivos = (mi_edad * 365)                                  # Hago la operacion aritmetica y guardo el resultado en la variable

print(f"Dias vividos:\t\t\t{dias_vivivos} dias")                # Muestro el resultado



#
# Ejercicio 12
#
soy_mayor = (mi_edad >= 18)                                     # Hago las operaciones de comparaciones y guardo el resultado en la variable

print(f"Soy mayor de edad?:\t\t{soy_mayor}")                    # Muestro el resultado



#
# Ejercicio 13
#
IMC_normal = (18.5 <= mi_IMC < 25)                              # Hago las operaciones de comparaciones y guardo el resultado en la variable

print(f"Mi IMC es normal?:\t\t{IMC_normal}")                    # Muestro el resultado



#
# Ejercicio 14
#
soy_mayor_y_estudiante = (soy_mayor and soy_estudiante)         # Hago la operacion AND y guardo el resultado en la variable

print(f"Soy mayor y estudiante?:\t{soy_mayor_y_estudiante}")    # Muestro el resultado



#
# Ejercicio 15
#
soy_mayor_o_estudiante = (soy_mayor or soy_estudiante)          # Hago la operacion OR y guardo el resultado en la variable

print(f"Soy mayor o estudiante?:\t{soy_mayor_o_estudiante}")    # Muestro el resultado



#
# Ejercicio 16
#
# Se puede dejar los valores en una variable, algo flexible pero mejorable
#distancia = 10
#velocidad = 12

# O se puede pedir los valores directamente al usuario, algo mucho mas flexible y mas general
print("\n\nPidiendo Datos")
distancia = float(input("Ingrese la distancia a recorrer: "))
velocidad = float(input("Ingrese la velocidad promedio: "))

horas = round(distancia / velocidad, 2)                         # Divido distancia por velocidad, guardo el resultado decimal
minutos = ((horas - int(horas)) * 60)                           # A eso le resto el entero y multiplico la parte decimal por 60
segundos = ((minutos - int(minutos)) * 60)                      # A eso le vuelvo a sacar el entero y multiplico la parte decimal por 60

horas = int(horas)                                              # Ya que tengo las horas, minutos y segundos guardados
minutos = int(minutos)                                          # convierto todo a enteros para mostrarlo por pantalla
segundos = int(segundos)

print("\nMostrando Datos")
# Muestro el timer en formato hora:minuto:segundo
print(f"{horas}:{minutos}:{segundos} se tardaria en recorrer {distancia}Kms a {velocidad}Km/h")



#
# Ejercicio 17
#
mi_altura_pulgadas = (mi_altura *  39.37)                       # Calculo y guardo mi altura en pulgadas
mi_altura_pulgadas = round(mi_altura_pulgadas, 2)               # Redondeo a 2 decimales el dato

print("\n\nMostrando Datos")
print(f"Mi altura en pulgadas es:\t{mi_altura_pulgadas} pulgadas")



#
# Ejercicio 18
#
mi_peso_libras = round((mi_peso * 2.20), 2)                     # Calculo, redondeo a 2 decimales y guardo mi peso en libres, todo en un solo paso

print(f"Mi peso en libras es:\t\t{mi_peso_libras} libras")        # Muestro el dato



#
# Ejercicio 19
#
# Se puede dejar los valores en una variable, algo flexible pero mejorable
#distancia = 100
#velocidad = 60

# O se puede pedir los valores directamente al usuario, algo mucho mas flexible y mas general
print("\n\nPidiendo Datos")
distancia = float(input("Ingrese la distancia a recorrer: "))
velocidad = float(input("Ingrese la velocidad promedio: "))


horas = round(distancia / velocidad, 2)                         # Divido distancia por velocidad, guardo el resultado decimal
minutos = ((horas - int(horas)) * 60)                           # A eso le resto el entero y multiplico la parte decimal por 60
segundos = ((minutos - int(minutos)) * 60)                      # A eso le vuelvo a sacar el entero y multiplico la parte decimal por 60

horas = int(horas)                                              # Ya que tengo las horas, minutos y segundos guardados
minutos = int(minutos)                                          # convierto todo a enteros para mostrarlo por pantalla
segundos = int(segundos)

print("\nMostrando Datos")
# Muestro el timer en formato hora:minuto:segundo
print(f"{horas}:{minutos}:{segundos} se tardaria en recorrer {distancia} millas a {velocidad} millas/h")



#
# Ejercicio 20
#
print("\n\nPidiendo Datos")
mi_color_favorito = input("Ingrese su color favorito: ")        # Pido por consola al usuario, que ingrese un valor alfabetico y lo guardo como cadena de caracteres (STRING)
longitud_color_favorito = len(mi_color_favorito)                # Obtengo como numero entero, la cantidad de caracteres en la cadena


print("\nMostrando Datos")
print(f"Mi color favorito es {mi_color_favorito} y tiene {longitud_color_favorito} letras")