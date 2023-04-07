import os

#
# Ejercicio 1
#
print("\n\nPidiendo Datos")
#mi_nombre = "Matias Lapenta"
mi_nombre = input("Ingrese su nombre: ")



#
# Ejercicio 2
#
#mi_edad = 30
mi_edad = int(input("Ingrese su edad: "))



#
# Ejercicio 3
#
#mi_altura = 1.64
mi_altura = float(input("Ingrese su altura: "))



#
# Ejercicio 4
#
#soy_estudiante = False
soy_estudiante = bool(int(input("Es estudiante? (1/0): ")))



#
# Ejercicio 5
#
print("\nMostrando Datos")
print(f"Mi nombre:\t{mi_nombre}")
print(f"Mi edad:\t{mi_edad} años")
print(f"Mi altura:\t{mi_altura} metros")
print(f"Es estudiante?:\t{soy_estudiante}")


#
# Ejercicio 6
#
print("\nTipos")
print(f"mi_nombre:\t{type(mi_nombre)}")
print(f"mi_edad:\t{type(mi_edad)}")
print(f"mi_altura:\t{type(mi_altura)}")
print(f"soy_estudiante:\t{type(soy_estudiante)}")


#
# Ejercicio 7
#
print("\n\nPidiendo Datos")
#mi_peso = 70
mi_peso = float(input("Ingrese su peso: "))

print("\nMostrando Datos")
print(f"Mi peso:\t\t{mi_peso}Kg")



#
# Ejercicio 8
#
mi_IMC = (mi_peso / (mi_altura ** 2))

print(f"Mi IMC:\t\t\t{mi_IMC}")



#
# Ejercicio 9
#
mi_IMC_redondeado = round(mi_IMC)

print(f"Mi IMC redondeado:\t{mi_IMC_redondeado}")



#
# Ejercicio 10
#
edad_en_5_años = mi_edad + 5

print("\n\nMostrando Datos")
print(f"Mi edad en 5 años:\t\t{edad_en_5_años} años")




#
# Ejercicio 11
#
dias_vivivos = (mi_edad * 365)

print(f"Dias vividos:\t\t\t{dias_vivivos} dias")



#
# Ejercicio 12
#
soy_mayor = (mi_edad >= 18)

print(f"Soy mayor de edad?:\t\t{soy_mayor}")



#
# Ejercicio 13
#
IMC_normal = (18.5 <= mi_IMC < 25)

print(f"Mi IMC es normal?:\t\t{IMC_normal}")



#
# Ejercicio 14
#
soy_mayor_y_estudiante = (soy_mayor and soy_estudiante)

print(f"Soy mayor y estudiante?:\t{soy_mayor_y_estudiante}")



#
# Ejercicio 15
#
soy_mayor_o_estudiante = (soy_mayor or soy_estudiante)

print(f"Soy mayor o estudiante?:\t{soy_mayor_o_estudiante}")



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
mi_color_favorito = input("Ingrese su color favorito: ")
longitud_color_favorito = len(mi_color_favorito)


print("\nMostrando Datos")
print(f"Mi color favorito es {mi_color_favorito} y tiene {longitud_color_favorito} letras")