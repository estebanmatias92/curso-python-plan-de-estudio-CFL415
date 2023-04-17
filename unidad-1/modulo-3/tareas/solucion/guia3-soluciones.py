import math
import random
from helpers import *

#
# Ejercicio 1
#
print("\n\n\nFuncion factorial")

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
print("\n\n\nFuncion numero primo")

# Funcion que toma un numero natural como argumento, comprueba si es primo y devuelve un valor booleano
def is_prime(num):

    if (num < 2) or (num > 2 and num % 2 == 0):                     # Si es menor a 2, o es mayor pero multiplo de 2, entonces no es primo
        return False                                                # Salgo devolviendo "False"
    else:
        raiz_num = math.ceil(math.sqrt(num))                        # Obtengo la raiz de "num" 

        for i in range(3, raiz_num, 2):                             # Recorro desde 3 hasta la raiz cuadrada de "num", pasando por todos los impares
            if (num % i == 0):                                      # Si "num" es multiplo de alguno esos numeros "i", entonces no es primo
                return False                                        # Devuelvo False y salgo

    return True                                                     # Si sobrevive hasta este punto, entonces es primo, devuelvo True y salgo


# Pido por consola un numero a comprobar su primalidad
mi_num = int(input("\nIngrese un numero natural: "))

# Llamo a la funcion para que se ejecute y me devuelva un valor y guardo ese valor en una variable
es_primo = is_prime(mi_num)

# Muestro los valores de esas variables en una oracion
print(f"El numero {mi_num} {'' if es_primo else 'no'} es primo")



#
# Ejercicio 3
#
print("\n\n\nFuncion MAXIMO COMUN DIVISOR")

# Esta tomo dos argumentos, Calcula el MCD y devuelve un valor entero
def get_mcd(a, b):

    minimo = min(a, b)                                              # Obtengo el menor de ambos

    for i in range(minimo, 0, -1):                                  # Empiezo desde el menor y recorro hasta el 1
        if (a % i == 0) and (b % i == 0):                           # Compruebo si algun valor entre "minimo" y 1 es multiplo de ambos
            return i                                                # Si encuentro tal valor, lo retorno y salgo


# Pido por consola dos numeros
num1 = int(input("\nIngrese primer numero natural: "))
num2 = int(input("Ingrese segundo numero natural: "))

# Llamo a la funcion para que se ejecute y me devuelva el maximo comun divisor
MCD = get_mcd(num1, num2)

# Muestro los valores de esas variables en una oracion
print(f"El Maximo Comun Divisor entre {num1} y {num2} es: {MCD}")



#
# Ejercicio 4
#
print("\n\n\nFuncion Minimo Comun Multiplo")

# Esta tomo dos argumentos, Calcula el MCD y devuelve un valor entero
def get_mcm(a, b):
    
    maximo = a if (a > b) else b                                    # Obtengo el maximo de ambos
    multiplicado = a * b                                            # Obtener una multiplicacion entre ambos

    for i in range(maximo, multiplicado  + 1):                      # Empiezo desde el mayor entre ambos y recorro hasta el 1
        if (i % a == 0) and (i % b == 0):                           # Compruebo si algun valor entre maximo y (a * b) es multiplo de ambos
            return i                                                # Si encuentro tal valor, lo retorno y salgo


# Pido por consola dos numeros
num1 = int(input("\nIngrese primer numero natural: "))
num2 = int(input("Ingrese segundo numero natural: "))

# Llamo a la funcion para que se ejecute y me devuelva el minimo comun multiplo
MCM = get_mcm(num1, num2)

# Muestro los valores de esas variables en una oracion
print(f"El Mimimo Comun Multiplo entre {num1} y {num2} es: {MCM}")



#
# Ejercicio 5
#
print("\n\n\nFuncion Suma de Digitos")

# Funcion que toma un numero entero como parametro, hace la sumatoria de sus digitos y devuelve el resultado
def sumar_digitos(num):

    suma = 0                                                        # Preparo la variable para acumular la suma

    while num:                                                      # Mientras "num" no sea 0, entonces itero
        digit = num % 10                                            # El resto de la division por 10 va a ser mi digito
        suma += digit                                               # Sumo el digito obtenido
        num //= 10                                                  # Actualizo el valor de "num" a partir de una division entera

    return suma                                                     # Una vez finalizado el bucle, retorno lo acumulado en "suma"


# Pido por consola un numero entero
mi_numero = int(input("\nIngrese un numero entero: "))

# Llamo a la funcion para que se ejecute y me devuelva la suma de los digitos
suma = sumar_digitos(mi_numero)

# Muestro los valores de esas variables en una oracion
print(f"La Suma de los digitos de {mi_numero} es: {suma}")



#
# Ejercicio 6
#
print("\n\n\nFuncion Comprobar Numero ARMSTRONG")

# Defino una funcion que toma un numero como parametro, verifica si es Armstrong y devuelve un valor booleano
def is_armstrong(num):

    if (num <= 0):                                                  # Primero que nada, compruebo que no sea cero o menor a cero
        return False                                                # Si es asi salgo

    i = num                                                         # Copio el valor en una variable nueva
    poweer = count_digits(num)                                      # Obtengo la cantidad de digitos en el numero
    suma = 0                                                        # Preparo la variable para la suma
    
    while i:                                                        # Itero mientras "i" no sea cero
        digit = (i % 10)                                            # Obtengo el digito 
        suma += (digit ** poweer)                                   # Suma el resultado del digito elevado a la cantidad de digitos   
        i //= 10                                                    # Actualizo el valor de "i" con los digitos restantes

    return (num == suma)                                            # Cuando el bucle termina, compruebo si el "num" original es igual a la suma de sus digitos y retorno el resultado booleano


# Pido por consola un numero entero
mi_numero = int(input("\nIngrese un numero entero: "))

# Llamo a la funcion para que se ejecute y me devuelva un valor booleano
es_armstrong = is_armstrong(mi_numero)

# Muestro los valores de esas variables
print(f"El numero {mi_numero} ", end="")
if (not es_armstrong):
    print(f"no ", end="")
print(f"es Armstrong")



#
# Ejercicio 7
#
print("\n\n\nFuncion Comprobar si Cadena es Numerica")

# Defino una funcion que toma un string como parametro, verifica si contiene solo numeros, y devuelve un valor booleano
def es_numerica(cadena):
    return cadena.isnumeric()


# Pido por consola una cadena de caracteres
mi_cadena = input("\nIngrese una cadena de caracteres: ")

# Llamo a la funcion para que se ejecute y me devuelva un valor booleano
es_numerica = es_numerica(mi_cadena)

# Muestro los valores de esas variables en una oracion
print(f"El string '{mi_cadena}' {'' if es_numerica else 'no '}es Numerico")



#
# Ejercicio 8
#
print("\n\n\nFuncion Comprobar si Cadena es Palindromo")

# Defino una funcion que toma un string como parametro, comprueba si es palindromo y devuelve un valor booleano
def is_palindrome(cadena):
    cadena_invertida = cadena[::-1]                                 # Otro modo de invertir una cadena es usando el operador [::-1]

    if (cadena != cadena_invertida):                                # Si al comparar ambos STRING, no son iguales, entonces devuelvo False
        return False

    return True                                                     # Sino devuelvo True


# Pido por consola una cadena de caracteres
mi_cadena = input("\nIngrese una palabra o frase: ")

# Llamo a la funcion para que se ejecute y me devuelva un valor booleano
es_palindromo = is_palindrome(mi_cadena)

# Muestro los valores de esas variables en una oracion
print(f"El string '{mi_cadena}' {'' if es_palindromo else 'no '}es Palindromo")



#
# Ejercicio 9
#
print("\n\n\nFuncion Convertir Decimal a Formato Tiempo")

# Defino una funcion que toma un numero decimal como parametro, convierte su valor a formato tiempo y devuelve la cadena.
def decimal_to_time(num):
    horas = round(num, 2)
    minutos = ((horas - int(horas)) * 60)
    segundos = ((minutos - int(minutos)) * 60)

    return (f"{int(horas)}:{int(minutos)}:{int(segundos)}")


# Pido por consola un numero decimal
mi_numero = float(input("\nIngrese un numero decimal: "))

# Llamo a la funcion para que se ejecute y me devuelva una cadena formateada en horas:minutos:segundos
formated_time = decimal_to_time(mi_numero)

# Muestro los valores de esas variables en una oracion
print(f"Decimal en formato tiempo (h:m:s) {formated_time}")



#
# Ejercicio 10
#
print("\n\n\nFuncion Multiplicacion")

# Defino una funcion que toma dos numeros, un multiplicando y un multiplicador, y retorna el multiplo o producto de ambos.
def multiplicar(multiplicand, multiplier):

    product = 0                                                     # Preparo la variable para guardar el resultado

    for i in range(1, multiplier + 1):                              # Recorro desde 1 hasta el multiplicador
        product += multiplicand                                     # Cada iteracion acumula la suma del multiplicando

    return product                                                  # Cuando sale del bucle, el resultado es devuelvo


# Pido por consola un numero entero
multiplicando = int(input("\nIngrese un numero a multiplicar: "))
multiplicador = int(input("Ingrese un multiplicador: "))

# Llamo a la funcion para que se ejecute y me devuelva un valor entero
multiplo = multiplicar(multiplicando, multiplicador)

# Muestro los valores de esas variables
print(f"El producto de {multiplicando} x {multiplicador} es: {multiplo}")



#
# Ejercicio 11
#
print("\n\n\nFuncion Contabilizar Vocales")

# Defino una funcion que toma una cadena, contabiliza la cantidad de vocales existentes y devuelve ese valor como numero entero.
def vowel_count(cadena):

    count = 0                                                       # Preparo la variable para guardar el resultado

    for c in cadena:                                                # Recorro la cadena, caracter por caracter
        if (c in "aeiou"):                                          # Si el caracter se encuentra entre as vocales
            count += 1                                              # Aumento el contador en 1
    
    return count                                                    # Al final del bucle retorno el valor acumulado


# Pido por consola una cadena de caracteres
mi_cadena = input("\nIngrese una palabra o frase: ")

# Llamo a la funcion para que se ejecute y me devuelva un valor entero
count = vowel_count(mi_cadena)

# Muestro los valores de esas variables
print(f"'{mi_cadena}' tiene {count} vocales")



#
# Ejercicio 12
#
print("\n\n\nFuncion Fibonacci")

# Funcion que toma un numero natural como argumento, obtengo su valor en la secuencia Fibonacci y devuelvo resultado
def fibonacci(num):
    
    if (num < 0):                                                   # Si "num" no cumple los requisitos para calcular la secuencia Fibonacci, se retorna cero
        return 0

    a = 0                                                           # Preparo los primeros valores de la serie Fib
    b = 1
    fib = 0

    for i in range(num):                                            # Arranco la serie hasta "num"
        fib = a                                                     # Salvo el ultimo valor "a", aparte
        a = b                                                       # Actualizo el valor de "a" por el de "b"
        b = fib + b                                                 # Ahora sumo el viejo valor de "a" + "b" y actualizo "b"
    
    return fib                                                      # Devuelvo el resultado final


# Pido el numero para calcular su fibonacci
mi_num = int(input("\nIngrese un numero natural: "))

# Llamo a la funcion para que se ejecute y me devuelva un valor entero
valor_retornado = fibonacci(mi_num)

# Muestro los valores de esas variables en una oracion
print(f"El fibonacci de {mi_num} es: {valor_retornado}")



#
# Ejercicio 13
#
print("\n\n\nFuncion Valor Absoluto")

# Funcion que toma un numero entero como argumento, obtengo su valor absoluto y devuelvo el resultado.
def get_absolute(num):
    
    if (num <  0):                                                  # Si el valor es negativo, lo convierto a positivo y lo devuelvo
        return -num
    
    return num                                                      # Si es positivo, lo devuelvo sin modificar

# Pido el numero para calcular su absoluto
mi_num = int(input("\nIngrese un numero entero: "))

# Llamo a la funcion para que se ejecute y me devuelva un valor entero
valor_retornado = get_absolute(mi_num)

# Muestro los valores de esas variables en una oracion
print(f"El valor absoluto de {mi_num} es: {valor_retornado}")


#
# Ejercicio 14
#
print("\n\n\nFuncion Contabilizar Frecuencia de una Letra")

# Defino una funcion que toma una cadena, contabiliza la cantidad de vocales existentes y devuelve ese valor como numero entero.
def char_count(cadena, letra):

    count = 0                                                       # Preparo la variable para guardar el resultado

    for c in cadena:                                                # Recorro la cadena, caracter por caracter
        if (c == letra):                                            # Si el caracter es igual a la letra buscada...
            count += 1                                              # Aumento el contador en 1
    
    return count                                                    # Al final del bucle retorno el valor acumulado


# Pido por consola una cadena de caracteres y una letra para buscar
mi_cadena = input("\nIngrese una palabra o frase: ")
mi_letra = input("Ingrese la letra a buscar: ")

# Llamo a la funcion para que se ejecute y me devuelva un valor entero
count = char_count(mi_cadena, mi_letra)

# Muestro los valores de esas variables
print(f"La letra '{mi_letra}' aparece {count} veces en '{mi_cadena}'")



#
# Ejercicio 15
#
print("\n\n\nFuncion Adivinar Numero del 1 al 100")

# Defino una funcion para generar y devolver un numero random entre "start" y "end"
def get_random(start, end):
    return random.randint(start, end)                               # Genero un numero entero random entre 1 y 100


# Defino una funcion para pedir el numero al usuario
def input_integer():
    return int(input("Ingrese un numero: "))                    


# Defino una funcion para comprobar si el numero adivinado es correcto o no, muestro pistas, y devuelvo un valor booleano
def adivinar(aleatorio, adivinanza):
    if (aleatorio < adivinanza):                                    # Sera menor?
        print("El numero que buscas es menor")
        return False
    elif (aleatorio > adivinanza):                                  # Sera mayor?
        print("El numero que buscas es mayor")
        return False
    
    return True                                                     # Si no es menor ni mayor es igual, entonce ha acertado


# Funcion principal del juego, es el bucle primario, donde sucede todo y desde donde se llama al resto de las funciones 
def juego_adivinar_random(intentos = 10):
    print("\nAdivine un numero entre 1 y 100!")                     # Titulo del juego

    numero_random = get_random(1, 100)                              # Obtengo el numero aleatorio para adivinar

    while intentos > 0:                                             # Entro en el bucle
        print(f"\nIntentos: {intentos}\n")                          # Muestro en cada pantalla los intentos restantes

        adivinanza = input_integer()                                # Pido el numero al usuario

        acierto = adivinar(numero_random, adivinanza)               # Intento adivinar, y/o tiro pistas

        if (acierto):                                               # Si adivino bien...
            break                                                   # Salgo del bucle
        else:
            intentos -= 1                                           # Sino continuo restando intentos

    if (acierto):                                                   # Si adivine bien..
        print(f"Ganaste!, has acertado al numero!")                 # Muestro mensaje de victoria
    else:                                                          
        print(f"Perdiste, el numero era ({numero_random})")         # Sino muestro el mensaje de derrota


# Llamo a mi funcion principal (main) del juego desde donde empieza a ejecutarse todo
juego_adivinar_random()
