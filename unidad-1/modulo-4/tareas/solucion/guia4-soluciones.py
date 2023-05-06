# Import generic system libs
import sys
import os

# Set the current and base directories
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..', '..'))
sys.path.insert(0, base_dir)

# Import module related libs
import math
import random
from recursos.helpers import *


#
# Funcion que toma un mensaje (STRING) y una funcion anonima (Lambda).
# La funcion prepara una lista vacia y pide los STRING al usuario con un bucle
#   que tiene como condicion de corte la funcion lambda obtenida como parametro
#
# Parametros:
#   (str) msg
#   (lambda) break_condition
#
# Retorno:
#   (list) lista
#
def input_lista(msg: str, break_condition = (lambda x: x.lower() == "n")):
    lista = []

    while True:
        elemento = input(msg)

        if break_condition(elemento):
            break

        lista.append(elemento)

    return lista


#
# Ejercicio 1
#
print("\n\n\nFuncion Factorial")

# Funcion que toma un numero natural como argumento, multiplica desde 1 hasta num, y devuelve un entero
def factorial(num):
    
    fac = 1

    for i in range(1, num + 1):                                     # Tipico FOR de un factorial
        fac *= i
    
    return fac                                                      # Retorno el valor acumulado y finalizo la ejecucion de la funcion


# Pido el numero para calcular su factorial
mi_num = int(input("\nIngrese un numero natural: "))

# Llamo a la funcion para que se ejecute y me devuelva un valor y guardo ese valor en una variable
valor_retornado = factorial(mi_num)

# Muestro los valores de esas variables en una oracion
print(f"El factorial de {mi_num}! es: {valor_retornado}")



#
# Ejercicio 2
#
print("\n\n\nFuncion Tupla Impares")

# Funcion que toma una tupla de numeros y devuelve una tupla con solo los impares
def get_odd_tuple(numbers: tuple) -> tuple:
    
    odd_list = []                                                   # Preparo una nueva lista

    for num in numbers:                                             # Recorro la tupla de numeros
        if (is_odd(num)):                                           # Compruebo si es impar
            odd_list.append(num)                                    # Agrego a la lista si se cumple la condicion
    
    return tuple(odd_list)                                          # Retorno los impares convertidos a tupla


# Pido numeros para generar un rango
num1 = int(input("\nIngrese un numero inicial para el rango: "))
num2 = int(input("Ingrese un numero limite para el rango: "))
start = min(num1, num2)
end = max(num1, num2)

# Genero el rango y lo convierto a tupla
numeros_generados = tuple(range(start, end + 1))
# Llamo a la funcion que me filtre los impares y los devuelva como tupla
impares = get_odd_tuple(numeros_generados)

# Muestro los valores de esas variables en dos oraciones
print(f"La tupla original es: {numeros_generados}")
print(f"La tupla impar es: {impares}")



#
# Ejercicio 3
#
print("\n\n\nPromedio Dia Caluroso")

# Creo el diccionario y lo inicializo en Cero
temperatures = {
    "lunes": None,
    "martes": None,
    "miercoles": None,
    "jueves": None,
    "viernes": None,
    "sabado": None,
    "domingo": None
}
hottest_day = None                                                  # Aca se guardara la clave (key), osea, el dia de la semana
hottest_temperature = float("-inf")                                 # (-Inf)inito, primer temperatura para contrastar

# Uso un bucle parar recorrer las claves del diccionario, y asigno sus valores con el input del usuario
for day in temperatures.keys():
    temperatures[day] = int(input(f"Ingrese la temperatura para el dia {day}: "))


for day, temperature in temperatures.items():                       # Recorro el diccionario, guardando su clave y valor, cada vez
    if (temperature > hottest_temperature):                         # Comparo el valor con la ultima temperatura mas alta
        hottest_day = day                                           # Si la nueva temperatura es mayor, guardo aparte el dia,
        hottest_temperature = temperature                           # y la temperatura 


# Muestro los valores de esas variables en una oracion
print(f"El dia mas caluroso fue {hottest_day}, con una temperatura de {hottest_temperature}")



#
# Ejercicio 4
#
print("\n\n\nFuncion Conjunto Pares")

# Funcion que toma un conjunto de numeros y devuelve un conjunto con solo los pares
def get_even_set(numbers: set) -> set:
    
    even_list = []                                                  # Preparo una nueva lista

    for num in numbers:                                             # Recorro la tupla de numeros
        if (is_even(num)):                                          # Compruebo si es impar
            even_list.append(num)                                   # Agrego a la lista si se cumple la condicion
    
    return set(even_list)                                           # Retorno los impares convertidos a tupla


# Pido numeros para generar un rango
num1 = int(input("\nIngrese un numero inicial para el rango: "))
num2 = int(input("Ingrese un numero limite para el rango: "))
start = min(num1, num2)
end = max(num1, num2)

# Genero el rango y lo convierto a conjunto
numeros_generados = set(range(start, end + 1))
# Llamo a la funcion que me filtre los pares y los devuelva como conjunto
pares = get_even_set(numeros_generados)

# Muestro los valores de esas variables en dos oraciones
print(f"El conjunto original es: {numeros_generados}")
print(f"El conjunto par es: {pares}")



#
# Ejercicio 5
#
print("\n\n\nOrdenar una lista de STRINGS")

# Funcion que toma dos parametros, una lista de strings y un booleano (opcional) y devuelve una lista ordenada por tamaño de strings
# El orden depende del valor del segundo parametro
def ordenar_lista(lista, ascendente = True):
    lista_copia = lista[:]                                          # Duplico la lista, la original, va a ser modificada
    lista_ordenada = []                                             # Preparo una variable para guardar mi lista ordenada luego

    while lista_copia:                                              # Empiezo a recorrer una por una las cadenas o STRINGS
        elemento = lista_copia[0]                                   # Obtengo el primer valor para comparar

        for cadena in lista_copia:                                  # Dentro del bucle While, vuelvo a recorrer todos los elementos para compararlos
            if ascendente:
                if len(cadena) > len(elemento):                     # Comparo si la cadena actual es mayor
                    elemento = cadena                               # Actualizo el valor de "elemento" con una cadena mayor
            else:
                if len(cadena) < len(elemento):                     # Comparo si la cadena actual es menor
                    elemento = cadena                               # Actualizo el valor de "elemento" con una cadena menor

        lista_ordenada.append(elemento)                             # Al final de todas las comparaciones, agrego el nuevo elemento a mi lista_ordenada
        lista_copia.remove(elemento)                                # y remuevo el mismo elemento de mi lista original, asi no lo comparo de nuevo
    
    return lista_ordenada                                           # Al final de TODOS los bucles, me queda solo la lista ordenada, y la original vacia


# Pido los STRING al usuario con un bucle y devuelvo una lista
lista = input_lista("Ingrese una palabra/frase o ingrese (N/n) para salir: ")

# Otro modo de hacer lo mismo es con la funcion sorted, que toma 3 parametros
# 1ro: La lista a ordenar
# 2do: La funcion que se va a usar para comparar cada elemento 
# 3ro: El orden en el cual se va a ordenar la lista
#lista_ordenada = sorted(lista, key=len, reverse=True)

# Llamo a mi funcion para que me devuelva una lista ORDENADA de STRINGS
lista_ordenada = ordenar_lista(lista, True)                         

# Muestro los valores de esas variables en dos oraciones
print(f"La lista original es: {lista}")
print(f"La lista ordenada es: {lista_ordenada}")



#
# Ejercicio 6
#
print("\n\n\nFuncion Tupla con Vocales")

# Funcion que toma una tupla de cadenas y devuelve una tupla de cadenas que empeizan por vocal
def vowel_first_strings(cadenas):
    vocales_primero = []                                            # Preparo la lista para guardar los STRINGS con vocales

    for cadena in cadenas:                                          # Recorro todas las tuplas
        if is_vowel(cadena[0]):                                     # Compruebo si el primer caracter de cada cadena, es una vocal
            vocales_primero.append(cadena)                          # Si lo es, lo añado a la lista

    return tuple(vocales_primero)                                   # Esa lista luego es convertida a tupla, y luego es devuelta


# Ppido los STRING al usuario con un bucle, devuelvo una lista y la convierto en tupla
cadenas = tuple(input_lista("Ingrese una palabra/frase o ingrese (N/n) para salir: "))
# Llamo a mi funcion para que me devuelva una tupla de STRINGS con primera letra vocal
cadenas_vocales = vowel_first_strings(cadenas)

# Muestro los valores de esas variables en dos oraciones
print(f"La tupla original es: {cadenas}")
print(f"La tupla con primera letra vocal es: {cadenas_vocales}")



#
# Ejercicio 7
#
print("\n\n\nPersona mas Vieja")

# Funcion que crea un diccionario y le va asignando datos de personas con un bucle.
# Cada nombre es la clave o key del diccionario y la edad es el valor.
def input_personas():
    personas = dict()                                               # Preparo el diccionario vacio

    while True:                                                     # Inicio el bucle
        nombre = input("\nIngrese el nombre: ")                     # Pido un string para el nombre
        edad = int(input("Ingrese la edad: "))                      # Pido un entero para la edad

        personas[nombre] = edad                                     # Añado esos valores al diccionario
        
        if (input("Desea continuar (Y/N): ").lower() == "n"):       # Compruebo si quiere seguir ingresando datos
            break                                                   # Salgo DEL BUCLE en caso de que no se quiera

    return personas                                                 # Al final de la funcion, retorno el diccionario que haya quedado


# Funcion que toma un diccionario con el nombre de personas como clave y la edad como valor, 
#   y retorna la persona mas joven
def get_youngest_person(personas: dict):
    persona_joven = {"nombre": None, "edad": float("inf")}          # Preparo el diccionario donde se guardara el individuo mas joven

    for nombre, edad in personas.items():                           # Recorro el diccionario, obteniendo clave y valor en cada iteracion
        if edad < persona_joven["edad"]:                            # Comparo edades
            persona_joven["nombre"] = nombre                        # Actualizo los datos si la nueva persona es mas joven
            persona_joven["edad"] = edad                                   

    return persona_joven                                            # Al final nos queda un diccionario con una unica persona, la mas joven


# Uso mi funcion para crear y rellenar el diccionario con datos de personas entradas por el usuario
datos_personas = input_personas()
# Uso mi funcion de filtrado, para buscar, encontrar y devolver, la persona mas joven de entre el diccionario                            
joven = get_youngest_person(datos_personas)

# Ahora muestro la info en ambos formatos, datos separados y diccionario entero
print(f"\nLa persona mas vieja tiene {joven['nombre']} y se llama {joven['edad']}, {joven}")



#
# Ejercicio 8
#
print("\n\n\nFiltrar Cadenas en Conjunto")

# Funcion que toma un conjunto como parametro, busca y filtra y devuelve un conjunto cadenas 
#   de mas de 5 caracteres
def filter_five_char_strings(conjunto: set):
    nuevo_conjunto = set()                                          # Creo el conjunto vacio, para guardar los filtrados luego

    for cadena in conjunto:                                         # Recorro el conjunto ingresado por parametro
        if len(cadena) >= 5:                                        # Compruebo si la cadena tiene 5 o mas caracteres
            nuevo_conjunto.add(cadena)                              # Si tiene 5 o mas, se añade al conjunto preparado
    
    return nuevo_conjunto                                           # Cuando termina la funcion se devuelve el conjunto rellenado


print("")

# Obtengo una lista de STRINGS o cadenas del usuario, lo convierto a conjunto y lo guardo en una variable
conjunto_strings = set(input_lista("Ingrese una palabra/frase o ingrese (N/n) para salir: "))
# Ahora filtro ese conjunto creado, lo devuelvo y lo guardo en una variable
conjunto_filtrado = filter_five_char_strings(conjunto_strings)

# Ahora muestro el conjunto de cadenas filtrado
print(f"El conjunto original es: {conjunto_strings}")
print(f"El conjunto filtrado es: {conjunto_filtrado}")



#
# Ejercicio 9
#
print("\n\n\nDiccionarios a Partir de Listas")

frutas = []                                                         # Preparo la lista para los nombres
precios = []                                                        # Preparo la lista para los precios

while True:                                                         # Comienzo mi bucle para rellenar las listas
    fruta = input("\nIngrese el nombre de una fruta: ")             # Pido el nombre
    precio = int(input("Ingrese el precio: "))                      # Pido el precio
    frutas.append(fruta)                                            # Añado el nombre a la lista correspondiente
    precios.append(precio)                                          # Añado el precio a la lista correspondiente
    
    if (input("Desea continuar (Y/N): ").lower() == "n"):           # Compruebo si quiere seguir ingresando datos
        break                                                       # Salgo DEL BUCLE en caso de que no se quiera


# Mezclo la lista de los nombres y la de los precios en un solo generador de tuplas, que luego es convertido en diccionario y guardado en la variable
lista_compras = dict(zip(frutas, precios))

# Ahora muestro el DICCIONARIO con las compras, con un bucle FOR
print("\nLa lista de Frutas es: ")
for fruta, precio in lista_compras.items():
    print(f"{fruta} - ${precio}")



#
# Ejercicio 10
#
print("\n\n\nListas Anidadas")

estudiantes = []                                                    # Preparo la lista para los ESTUDIANTES

while True:                                                         # Comienzo el bucle                
    datos = []                                                      # Preparo la lista anidada, DATOS
    nombre = input("\nIngrese el nombre del estudiante: ")          # Pido el nombre
    datos.append(nombre)                                            # Lo añado a la lista DATOS    
    for i in range(1, 3):
        datos.append(int(input(f"Ingrese la nota Nro {i}: ")))      # Pido y añado la nota a la lista DATOS
    
    estudiantes.append(datos)                                       # Finalizado todo el ingreso de datos, añado la lista anidada DATOS, a la lista padre ESTUDIANTES        

    if (input("Desea continuar (Y/N): ").lower() == "n"):           # Compruebo si quiere seguir ingresando datos
        break                                                       # Salgo DEL BUCLE en caso de que no se quiera


# Muestro la lista de estudiantes y sus notas
print(f"\n{estudiantes}")



#
# Ejercicio 11
#
print("\n\n\nPaises Euro-Asiaticos")

europa = {"Rusia", "Kazajistán", "Azerbaiyán", "Georgia", "Turquía"}
asia = {"Rusia", "Kazajistán", "Azerbaiyán", "Georgia", "Turquía", "China", "Japón"}

# Uso el metodo intersection del objeto set()
interseccion = europa.intersection(asia)

# Muestro el conjunto de paises  y sus notas
print(f"Países en Europa y Asia: {interseccion}")



#
# Ejercicio 12
#
print("\n\n\nFuncion Encontrar Apellidos en Lista")

fullnames = [                                                       # Preparo mi lista de elementos a filtrar
    "Pepito Gonzales",
    "Juancito Herrera",
    "Matias Peña",
    "Agustin Celaya"
]

lastnames = [                                                       # Preparo mi lista de targets
    "Herrera",
    "Peña"
]

# La funcion toma dos listas como argumento, la primera de nombres completos y la segunda de apellidos
# Filtra y devuelve una nueva lista con los nombres completos de la primera lista, cuyos apellidos, aparecen en la segunda
def filter_names(full_names, last_names):
    filtered_names = []                                             # Creo una lista para guardar los filtrados

    for full_name in full_names:                                    # Recorro los nombres completos
        last_name = full_name.split()[-1]                           # Convierto la frase en lista de palabras y obtengo la ultima

        if last_name in last_names:                                 # Si la ultima palabra (apellido), esta en mi lista target de apellidos
            filtered_names.append(full_name)                        # La agrego a mi lista de filtrados

    return filtered_names                                           # Al final de todo devuelvo los apellidos que haya filtrado


# Ahora muestro la lista de nombres completos filtrados
print(f"Los apellidos filtrados son: {filter_names(fullnames, lastnames)}")